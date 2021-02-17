import sys
from random import shuffle
from typing import List, NoReturn, Tuple
from PySide2 import QtWidgets
from ui_fifo_simulator import Ui_FifoSimulator
from fifo import processing
from worker import Worker


class MainWindow(QtWidgets.QMainWindow, Ui_FifoSimulator):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.start = False
        self.worker = None
        self.button_start_stop.clicked.connect(lambda: self.start_process())
        self.init_app_fifo()

    def start_process(self) -> NoReturn:
        """Método para start/stop, da Thread de consumo de processos.
        Return: NoReturn
        """
        if not self.start:
            self.button_start_stop.setText("Stop")
            self.start = True
            self.worker = Worker(processing)
            self.worker.signal.list_process.connect(self.set_queue)
            self.worker.signal.progress_signal.connect(self.progress_bar_value)
            self.worker.signal.progress_signal_percentage.connect(
                self.label_cpu_percentage.setText
            )
            self.worker.signal.result_output.connect(self.set_output)
            self.worker.start()

        else:
            self.worker.terminate()
            self.button_start_stop.setText("Start")
            self.start = False
            self.init_app_fifo()

    def set_queue(self, list_queue: Tuple) -> NoReturn:
        """Método para atualização da lista de processos e style.
        Arguments: - list_queue [tuple]
        Return: NoReturn
        """
        queue_process_label = [self.label_p1, self.label_p2, self.label_p3]
        queue_process_frame = [self.queue_p1, self.queue_p2, self.queue_p3]
        count = 0
        for i in range(list_queue[0], list_queue[0] + 3):
            style_sheet = (
                "QFrame {"
                f"background-color: rgb({list_queue[1][count][1]});"
                "}"
            )
            queue_process_label[count].setText(f"P{str(i)}")
            queue_process_frame[count].setStyleSheet(style_sheet)
            count += 1

    def progress_bar_value(self, value: List) -> NoReturn:
        """Método para atialização da barra de progresso.
        Arguments: - value [list]
        Return: NoReturn
        """
        progress = (100 - value[0]) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        style_sheet = (
            "QFrame {"
            "border-radius: 150px;"
            f"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop_1}"
            f" rgba(211, 215, 207, 0), stop:{stop_2} rgba({value[1]}, 255));"
            "}"
        )
        self.circular_progress.setStyleSheet(style_sheet)

    def init_app_fifo(self) -> NoReturn:
        """Método para inicio do App.
        Return: NoReturn
        """
        self.progress_bar_value([0, "136, 138, 133"])
        self.label_cpu_percentage.setText("")
        list_bar_proc_queue = [
            self.process_bar_f0,
            self.process_bar_f1,
            self.process_bar_f2,
            self.process_bar_f3,
            self.process_bar_f4,
            self.process_bar_f5,
            self.process_bar_f6,
        ]
        list_labels = [
            self.label_ready_p,
            self.label_in_exec_p,
            self.cpu_time_value,
            self.cpu_idle_value,
            self.cpu_busy_value,
            self.wait_max,
            self.wait_mean,
            self.wait_min,
            self.label_pid_0,
            self.label_pid_1,
            self.label_pid_2,
            self.label_pid_3,
            self.label_pid_4,
            self.label_pid_5,
            self.label_pid_6,

        ]
        for process_bar_f in list_bar_proc_queue:
            process_bar_f.setVisible(False)
        for label in list_labels:
            label.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
