import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import flask
import flask_restful

import celery
import flask_rabbitmq
import flask_sqlalchemy
import flask_uploads
import flask_httpauth
import flask_elasticsearch

from setting import conf

from log import get_logger

app = flask.Flask(__name__)
app.config.from_object(conf)

from app.api import blueprint as api_blueprint
from app.auth import blueprint as auth_blueprint
from app.login import blueprint as login_blueprint
from app.blog import blueprint as blog_blueprint

# 默认
app.register_blueprint(login_blueprint)

# login
app.register_blueprint(login_blueprint, url_prefix="/login")

# api
app.register_blueprint(api_blueprint, url_prefix="/api")

# auth
app.register_blueprint(auth_blueprint, url_prefix="/auth")

# blog
app.register_blueprint(blog_blueprint, url_prefix="/blog")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=6785,
        debug=True
    )
