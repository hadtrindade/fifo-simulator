from queue import Queue
from random import randint
from functools import wraps
from time import sleep
from os import getpid


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


def processing(
    progress_signal_percentage=None,
    progress_signal=None,
    list_process=None,
):
    count = 0
    while True:
        value = queue_fifo.get()
        list_process.emit((count, get_full_queue()))
        print(count)
        for i in range(value):
            sleep(0.5)
            progress_signal.emit(i / value * 100)
            progress_signal_percentage.emit(str(round(i / value * 100)) + "%")
        count += 1
