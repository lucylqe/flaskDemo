import os
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    STATIC_FOLDER = os.path.join(ROOT_PATH, "static")
    UPLOAD_FOLDER = os.path.join(ROOT_PATH, "static/upload")
    UPLOADED_PHOTOS_DEST = os.path.join(ROOT_PATH, "static/upload/images")
    UPLOADED_VIDEO_DEST = os.path.join(ROOT_PATH, "static/upload/video")
    MEIYAN_PHOTOS_DEST = os.path.join(ROOT_PATH, "static/meiyan")

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    # REDIS = 'redis://:liqe123@localhost:6379'
    REDIS = 'redis://:build_local@192.168.195.179:6379'


    # mysql数据库连接信息,这里改为自己的账号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://build_local:build_local@127.0.0.1:3306/ocr"

    @staticmethod
    def init_app(app):
        pass

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
version = os.environ.get('FLASK_ENV', 'development')
conf = confmap.get(version)




