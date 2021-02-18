import sys
from typing import List, NoReturn, Tuple
from PySide2 import QtWidgets
from ui_fifo_simulator import Ui_FifoSimulator
from fifo import processing, clock
from worker import Worker
from time import sleep


class MainWindow(QtWidgets.QMainWindow, Ui_FifoSimulator):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.start = False
        self.worker = None
        self.cpu_busy = None
        self.current_time = None
        self.process_time = []
        self.button_start_stop.clicked.connect(lambda: self.start_process())
        self.init_app_fifo()

    def start_process(self) -> NoReturn:
        """Método para start/stop, da Thread de consumo de processos.
        Return: NoReturn
        """
        if not self.start:
            self.button_start_stop.setText("Stop")
            self.start = True

            self.worker_clock = Worker(clock)
            self.worker_clock.signal.clock_signal.connect(self.set_clock)
            self.worker_clock.start()
            sleep(0.1)

            self.worker = Worker(processing)
            self.worker.signal.list_process.connect(self.set_queue)
            self.worker.signal.progress_signal.connect(self.progress_bar_value)
            self.worker.signal.clock_signal.connect(self.set_clock)
            self.worker.signal.cpu_busy_signal.connect(self.set_idle_time)
            self.worker.signal.progress_signal_process.connect(
                self.process_bar_f0.setValue
            )
            self.worker.signal.progress_signal_process_run.connect(
                self.label_in_exec_p.setText
            )
            self.worker.signal.progress_signal_process_ready.connect(
                self.label_ready_p.setText
            )
            self.worker.signal.progress_signal_percentage.connect(
                self.label_cpu_percentage.setText
            )
            self.worker.start()

        else:
            self.worker_clock.terminate()
            self.worker.terminate()
            self.button_start_stop.setText("Start")
            self.start = False
            self.init_app_fifo()

    def set_queue(self, list_queue: Tuple) -> NoReturn:
        """Método para atualização da lista de processos e style.
        Arguments: - list_queue [tuple]
        Return: NoReturn
        """
        queue_process_label = [
            self.label_pid_0,
            self.label_pid_1,
            self.label_pid_2,
            self.label_pid_3,
            self.label_pid_4,
            self.label_pid_5,
            self.label_pid_6,
        ]
        queue_process_bars = [
            self.process_bar_f0,
            self.process_bar_f1,
            self.process_bar_f2,
            self.process_bar_f3,
            self.process_bar_f4,
            self.process_bar_f5,
            self.process_bar_f6,
        ]

        count = 0
        geometry_x = 350
        self.process_time.append(list_queue[0])
        self.wait_min.setText(str(0))
        for i in range(list_queue[0], list_queue[0] + 7):
            style_sheet = (
                "QProgressBar {"
                "color:  rgb(69, 69,69);"
                "border: 0px solid;"
                "border-radius: 5px;"
                "border-style: none;"
                "background-position: center;"
                "text-align: center;"
                f"background-color: rgb({list_queue[1][count][1]});"
                "}"
                "QProgressBar::chunk {"
                "background-color: rgb(238, 238, 236);"
                "}"
            )
            queue_process_label[count].setText(f"PID{str(i)}")
            queue_process_bars[count].setStyleSheet(style_sheet)
            geometry = [
                geometry_x,
                (200 + (100 - (list_queue[1][count][0]) * 10)),
                50,
                ((list_queue[1][count][0]) * 10),
            ]
            queue_process_bars[count].setGeometry(*geometry)
            count += 1
            geometry_x += 60
        time_avarege = sum(self.process_time) / len(self.process_time) * 100
        self.wait_mean.setText(str(time_avarege))
        self.wait_max.setText(str(sum(self.process_time) * 100))

    def set_clock(self, value):
        self.current_time = value
        self.cpu_time_value.setText(str(self.current_time))
        if self.cpu_busy:
            self.cpu_busy_value.setText(str(self.current_time - self.cpu_idle))

    def set_idle_time(self, value):
        self.cpu_idle_value.setText(str(self.current_time))
        self.cpu_idle = self.current_time
        self.cpu_busy = value

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
        style_sheet = """QProgressBar 
                        {
                            border: 0px solid;
                            border-style: none;
                            }
                            """
        for process_bar_f in list_bar_proc_queue:
            process_bar_f.setStyleSheet(style_sheet)
            process_bar_f.setValue(0)
        for label in list_labels:
            label.setText("")
        self.cpu_busy = None
        self.current_time = None
        self.process_time = []


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
