from queue import Queue
from random import randint
from functools import wraps


queue_fifo = Queue(maxsize=3)


def coroutine(func):
    @wraps(func)
    def primer():
        gen = func()
        next(gen)
        return gen
    return primer


@coroutine
def gen_next_process():
    while True:
        yield randint(3, 9)


def get_full_queue():
    while True:
        if not queue_fifo.full():
            queue_fifo.put(next(gen_next_process()))
        else:
            return list(queue_fifo.queue)
