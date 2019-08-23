import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# init root logger
# 修改flask日志输出默认行为--使其最终输出到日志文件和控制台
# Flask框架在处理完请求后，调用了werkzeug库的_log函数；用的root loger即name=None
# apps.logger.debug('a') 用的是名称为flask.app的logger
from log import get_logger

logger = get_logger(name=None, clear_handlers=True)


def register_blueprints(root, app):
    from werkzeug.utils import find_modules, import_string
    from itertools import chain

    for name in chain([root], find_modules(root, recursive=True, include_packages=True)):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            name = name[len(root) + 1:]
            prefix = "/" + "/".join(name.split('.'))
            app.register_blueprint(mod.blueprint, url_prefix=prefix)


# 优先使用当前蓝图的模板
# def improve_blueprint_template_nice(app):
#     def before_request():
#         from flask import request
#         if request.blueprint is not None:
#             bp = app.blueprints[request.blueprint]
#             if bp.jinja_loader is not None:
#                 newsearchpath = bp.jinja_loader.searchpath + app.jinja_loader.searchpath[-1:]
#                 app.jinja_loader.searchpath = newsearchpath
#                 print(app.jinja_loader.searchpath)
#             else:
#                 app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
#         else:
#             app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
#     return before_request

def make_app():
    from flask import Flask
    app = Flask(__name__)

    from setting import config
    app.config.from_object(config)

    # 加载第三方扩展  先完成初始化 再加载蓝图 防止蓝图中用到未初始化的第三方插件
    from extension import  mysqldb, esdb, bootstrap, celery
    mysqldb.init_app(app)
    esdb.init_app(app)
    bootstrap.init_app(app)
    celery.init_app(app)

    # 注册试图路由
    register_blueprints('apps', app)


    #提高蓝图模板优先级
    # app.before_request(improve_blueprint_template_nice(app))

    #打印urls映射
    for k in list(sorted(app.url_map.iter_rules(), key=lambda e:str(e))):
        print(repr(k))
    return app
