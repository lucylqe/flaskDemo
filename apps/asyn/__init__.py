from flask import render_template
from apps.libs.register_blueprint import NestableBlueprint

blueprint = bp = NestableBlueprint(cur_name=__name__, cur_file=__file__)


@bp.route('/celery')
def celery_plus_one():
    from apps.asyn.celery_task.example import plus_one
    # 发送异步任务，指定队列
    plus_one.apply_async(args=[5])
    return str(plus_one)


@bp.route('/concurrent')
def concurrent_plus_one():
    from apps.asyn.concurrent_task.example import thread_pool, plus_one_wait
    # 发送异步任务，指定队列
    futures = [(pair, thread_pool.submit(plus_one_wait, pair)) for pair in range(1, 2)]
    for pair, future in futures:
        print('[{}]执行中:{}, 已完成:{}'.format(pair, future.running(), future.done()))
    return str(futures)