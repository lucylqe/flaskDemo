import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# init root logger
# 修改flask日志输出默认行为--使其最终输出到日志文件和控制台
# Flask框架在处理完请求后，调用了werkzeug库的_log函数；用的root loger即name=None
# apps.logger.debug('a') 用的是名称为flask.app的logger
from log import get_logger
_ = get_logger(None, filename='access', clear_handlers=True, userid_format=False)



def register_blueprints(root, app):
    from werkzeug.utils import find_modules, import_string
    from itertools import chain

    for name in chain([root], find_modules(root, recursive=True, include_packages=True)):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            name = name[len(root)+1:]
            prefix = "/" + "/".join(name.split('.'))
            app.register_blueprint(mod.blueprint, url_prefix=prefix)

def make_app():
    from flask import Flask
    app = Flask(__name__)

    from setting import conf
    app.config.from_object(conf)

    # 注册试图路由
    register_blueprints('apps', app)

    # 加载第三方扩展
    from extension import api, mysqldb, esdb
    api.init_app(app)
    mysqldb.init_app(app)
    esdb.init_app(app)

    return app
