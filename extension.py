import flask_restful
import celery
import flask_rabbitmq
import flask_sqlalchemy
import flask_uploads
import flask_httpauth
import flask_elasticsearch
import flask_bootstrap



api = flask_restful.Api()
mysqldb = flask_sqlalchemy.SQLAlchemy()
esdb = flask_elasticsearch.FlaskElasticsearch()
bootstrap = flask_bootstrap.Bootstrap()