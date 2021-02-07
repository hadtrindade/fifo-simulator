from queue import Queue
from typing import Generator, List, Callable, NoReturn
from random import randint
from functools import wraps
from time import sleep


queue_fifo = Queue(maxsize=3)


def coroutine(func: Callable) -> Generator:
    """Função decoradora que recebe um invocável"""

    @wraps(func)
    def primer():
        gen = func()
        next(gen)
        return gen

    return primer


@coroutine
def gen_next_process() -> Generator:
    """Função geradora para geração dos processos."""
    while True:
        yield randint(3, 9)


def get_full_queue() -> List:
    """Função que retorna uma lista contendo os elementos da FILA FIFO."""
    while True:
        if not queue_fifo.full():
            rgb = f"{randint(0,255)},{randint(0,255)},{randint(0,255)}"
            queue_fifo.put([next(gen_next_process()), rgb])
        else:
            return list(queue_fifo.queue)


def processing(
    progress_signal_percentage: Callable,
    progress_signal: Callable,
    list_process: Callable,
    result_output: Callable,
) -> NoReturn:
    """Função responsável pelo processamento e exibição do progresso."""
    count = 0
    while True:
        list_process.emit((count, get_full_queue()))
        value = queue_fifo.get()
        for i in range(1, value[0] + 1):
            sleep(0.5)
            progress_signal.emit([(i / value[0] * 100), value[1]])
            progress_signal_percentage.emit(
                str(round(i / value[0] * 100)) + "%"
            )
        result_output.emit(randint(0, 5))
        count += 1
