from extension import celery

from celery import Celery
assert isinstance(celery, Celery)

@celery.task(bind=True)
def plus_one(self, x):
    print(self, x)
    return x + 1


@celery.task(name='heartbeat')
def heartbeat():
    print('send heartbeat')