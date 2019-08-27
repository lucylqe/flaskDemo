bind = ["127.0.0.1:3434"]

backlog = 2048
workers = 2
keepalive = 5
worker_class = "gevent"

######################################################################
##                       SCRIPT                                     ##
######################################################################
import os
from log import get_logger

logger = get_logger()

if 'CUDA_VISIBLE_DEVICES' in os.environ:
    logger.info('GET CUDA_VISIBLE_DEVICES')
    key = 'CUDA_VISIBLE_DEVICES'
    key_used = 'USED_PER_PROCESS'


    def gpus_allocation():
        if key_used not in os.environ:
            os.environ[key_used] = '1'
        gpus_used = float(os.environ.get(key_used))
        gpus_list = os.environ.get(key, '').split(',')
        logger.info("{}|{}".format(gpus_list, gpus_used))
        assert gpus_used * workers <= len(gpus_list)
        i = 0
        for gpusid in gpus_list:
            while i + gpus_used <= 1:
                yield gpusid
                i += gpus_used
            i = 0


    gpus = gpus_allocation()


    def alloc_gpus():
        gpusid = next(gpus)
        os.environ[key] = str(gpusid)

else:
    alloc_gpus = lambda: None


def on_starting(server):
    logger.info("[LIQE][on_starting][{}][{}]".format(server, server))


def on_reload(server):
    logger.info("[LIQE][on_reload][{}][{}]".format(server, server))


def when_ready(server):
    logger.info("[LIQE][when_ready][{}][{}]".format(server, server))


def pre_fork(server, worker):
    alloc_gpus()
    logger.info("[LIQE][pre_fork][{}][{}]".format(server, worker))


def post_fork(server, worker):
    logger.info("[LIQE][post_fork][{}][{}]".format(server, worker))


def post_worker_init(worker):
    logger.info("[LIQE][post_worker_init][{}]".format(worker))


def worker_int(worker):
    logger.info("[LIQE][worker_int][{}]".format(worker))


def worker_abort(worker):
    logger.info("[LIQE][worker_abort][{}]".format(worker))


def pre_exec(server):
    logger.info("[LIQE][pre_exec][{}]".format(server))


def pre_request(worker, req):
    logger.info("[LIQE][pre_request][{}][{}]".format(worker, req))


def post_request(worker, req, environ, resp):
    pass
    # logger.info("[LIQE][post_request][{}][{}][{}][{}]".format(worker, req, environ, resp))


def child_exit(server, worker):
    logger.info("[LIQE][child_exit][{}][{}]".format(server, worker))


def worker_exit(server, worker):
    logger.info("[LIQE][worker_exit][{}][{}]".format(server, worker))


def nworkers_changed(server, new_value, old_value):
    logger.info("[LIQE][nworkers_changed][{}][{}][{}]".format(server, new_value, old_value))


def on_exit(server):
    logger.info("[LIQE][on_exit][{}]".format(server))