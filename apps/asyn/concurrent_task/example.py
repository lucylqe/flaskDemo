from concurrent.futures import ThreadPoolExecutor
thread_pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix='ThreadPoolExecutor')

def plus_one_wait(x):
    import time
    time.sleep(5)
    res = x + 1
    print('plus_one args[{}] 已完成, 结果[{}]'.format(x, res))