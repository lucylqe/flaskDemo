import flask_restful
import celery
import flask_rabbitmq
import flask_sqlalchemy
import flask_uploads
import flask_httpauth
import flask_elasticsearch


mysqldb = flask_sqlalchemy.SQLAlchemy()
esdb = flask_elasticsearch.FlaskElasticsearch()