from celery import Celery as CeleryClass
import flask_rabbitmq
import flask_sqlalchemy
import flask_uploads
import flask_httpauth
import flask_elasticsearch
import flask_bootstrap

mysqldb = flask_sqlalchemy.SQLAlchemy()
esdb = flask_elasticsearch.FlaskElasticsearch()
bootstrap = flask_bootstrap.Bootstrap()


class Celery(CeleryClass):
    def __init__(self):
        self.init = super(Celery, self).__init__

    def init_app(self, app):
        from flask import Flask, Blueprint
        assert isinstance(app, (Flask, Blueprint))

        class ContextTask(celery.Task):
            abstract = True

            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        self.init(main=app.name,
                  broker=app.config.get('CELERY_BROKER_URL', None),
                  backend=app.config.get('CELERY_RESULT_BACKEND', None),
                  task_cls=ContextTask)
        self.config_from_object(app.config)
        TaskBase = celery.Task

celery = Celery()