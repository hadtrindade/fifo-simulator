from queue import Queue
from typing import List, Callable, NoReturn
from random import randint
from time import sleep


queue_fifo = Queue(maxsize=7)


def get_full_queue() -> List:
    """Função que retorna uma lista contendo os elementos da fila FIFO.
    Return:
     list -- contendo os elementos dafila.
    """
    while True:
        if not queue_fifo.full():
            rgb = f"{randint(0,255)},{randint(0,255)},{randint(0,255)}"
            queue_fifo.put([randint(3, 9), rgb])
        else:
            return list(queue_fifo.queue)


def processing(
    progress_signal_percentage: Callable,
    progress_signal: Callable,
    progress_signal_process: Callable,
    list_process: Callable,
    progress_signal_process_run: Callable,
    progress_signal_process_ready: Callable,
) -> NoReturn:
    """Função responsável pelo processamento e exibição de status do progresso."""
    count = 0
    while True:
        list_process.emit((count, get_full_queue()))
        value = queue_fifo.get()
        for i in range(1, value[0] + 1):
            sleep(0.5)
            progress_signal_process_run.emit(f"PID{count}")
            progress_signal_process_ready.emit(f"PID{count+1}")
            progress_signal.emit([(i / value[0] * 100), value[1]])
            progress_signal_process.emit(round(i / value[0] * 100))
            progress_signal_percentage.emit(
                str(round(i / value[0] * 100)) + "%"
            )
        count += 1
