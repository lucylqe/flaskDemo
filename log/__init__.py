import os
import logging

try:
    import colorlog
except:
    colorlog = None

from logging import getLogger, Formatter, StreamHandler, LoggerAdapter
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

curdir = os.path.abspath(os.path.dirname(__file__))
logsdir = os.path.join(curdir, 'logfiles')
if not os.path.exists(logsdir):
    os.mkdir(logsdir)

# 防止flask 对日志加控制台颜色； 输出到文件后可能会有一些不必要的颜色信息
# 调用链 [send_response, python3.6/site-packages/werkzeug/serving.py:332] -> [log_request, serving.py:373] -> [log, serving.py:384] -> [_log, _internal.py:88]
# 其中log_request函数会对 msg 用termcolor模块加控制台颜色
os.environ['ANSI_COLORS_DISABLED'] = 'true'


# logging.getLogger = lambda name:LoggerAdapter(getLogger(name), {'userid': 'default'})

def get_logger(name, filename=None, clear_handlers=False, special_formatter=True):
    filename = filename or name
    filepath = os.path.join(curdir, 'logfiles', f"{filename}")

    if special_formatter:
        formatter = f'%(asctime)s|%(process)d|%(filename)s|nm:%(lineno)d|%(levelname)s|%(userid)s|%(message)s'
    else:
        formatter = f'%(asctime)s|%(process)d|%(filename)s|nm:%(lineno)d|%(levelname)s|%(message)s'
    formatter_color = f'%(log_color)s' + formatter

    logger = logging.getLogger(name)
    # 防止信息往上级传递 eg: root loger
    # 如果配置上级logger，就会输出两边
    logger.propagate = False
    if clear_handlers and logger.handlers:
        logger.handlers.clear()

    # 控制台

    if colorlog:
        handler = colorlog.StreamHandler()
        fmt = colorlog.ColoredFormatter(formatter_color,
                                        datefmt=None,
                                        reset=True,
                                        log_colors={
                                            'DEBUG': 'cyan',
                                            'INFO': 'green',
                                            'WARNING': 'yellow',
                                            'ERROR': 'red',
                                            'CRITICAL': 'red,bg_white',
                                        },
                                        secondary_log_colors={
                                            # 'message': {
                                            #     'ERROR': 'yellow',
                                            #     'CRITICAL': 'yellow'}
                                        })
    else:
        fmt = Formatter(formatter)
        handler = StreamHandler()
    handler.setFormatter(fmt)
    logger.addHandler(handler)

    # 日志文件
    # fileSizeJandler = RotatingFileHandler(filepath, maxBytes=1024, backupCount=1)
    # fileSizeJandler.setFormatter(formatter)
    # logger.addHandler(fileSizeJandler)

    # 日志文件 按日期划分 DEBUG 开发使用
    fileTimeHandler = TimedRotatingFileHandler(filepath + '.debug.log', "D", 1, 10)
    fileTimeHandler.suffix = "%Y%m%d.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
    fileTimeHandler.setFormatter(Formatter(formatter))
    fileTimeHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileTimeHandler)

    # 日志文件 按日期划分 INFO 生产使用
    fileTimeHandler = TimedRotatingFileHandler(filepath + '.info.log', "D", 1, 10)
    fileTimeHandler.suffix = "%Y%m%d.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
    fileTimeHandler.setFormatter(Formatter(formatter))
    fileTimeHandler.setLevel(logging.INFO)
    logger.addHandler(fileTimeHandler)

    non_error_filter = logging.Filter()
    non_error_filter.filter = lambda record: record.levelno < logging.WARNING
    fileTimeHandler.addFilter(non_error_filter)

    # 日志文件 按日期划分  ERROR 生产使用
    fileTimeHandler = TimedRotatingFileHandler(filepath + '.error.log', "D", 1, 10)
    fileTimeHandler.suffix = "%Y%m%d.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
    fileTimeHandler.setFormatter(Formatter(formatter))
    fileTimeHandler.setLevel(logging.ERROR)
    logger.addHandler(fileTimeHandler)

    logger.setLevel(logging.DEBUG)

    # LoggerAdapter 每个用户可以持有一个adapter. 便可添加额外信息
    # new_loger=LoggerAdapter(logger.logger, {'userid':'liqe'})
    return LoggerAdapter(logger, {'userid': 'default'})


# Flask框架在处理完请求后，调用了werkzeug库的_log函数；用的root loger即name=None
# app.logger.debug('a') 用的是名称为flask.app的logger
# init root logger
_ = get_logger(None, filename='access', clear_handlers=True, special_formatter=False)

if __name__ == '__main__':
    a = get_logger('test1')
    a.debug('debug')
    a.info('info')
    a.warning('warning')
    a.error('error')
    a.critical('critical')
