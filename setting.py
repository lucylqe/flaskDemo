import os
from datetime import timedelta
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


class Config(dict):
    def __init__(self):
        dict.__init__(self)

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            return getattr(self, item)

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


    # mysql数据库连接信息,这里改为自己的账号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:test@127.0.0.1:3306/test"

    # redis
    REDIS = 'redis://:liqe123@localhost:6379'


    # 定时任务配置
    CELERY_BROKER_URL = REDIS + '/1'
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERYBEAT_SCHEDULE = {
        'heartbeat': {
            'task': 'heartbeat',
            'schedule': timedelta(minutes=1),
            'args': ()
        },
    }



class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


confmap = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

import os

env = os.environ.get('FLASK_ENV', 'development')
config = confmap.get(env)()