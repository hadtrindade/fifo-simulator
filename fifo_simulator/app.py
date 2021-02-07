import sys
from PySide2 import QtWidgets
from ui_fifo_simulator import Ui_FifoSimulator
from fifo import queue_fifo, get_full_queue, processing
from worker import Worker


class MainWindow(QtWidgets.QMainWindow, Ui_FifoSimulator):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.queue_process = get_full_queue()
        self.queue = queue_fifo
        self.start = False
        self.worker = None
        self.button_start_stop.clicked.connect(lambda: self.start_process())
        self.init_app_fifo()

    def start_process(self):
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

    def set_queue(self, list_queue):
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

    def set_output(self, value):
        tasks = [
            "image: url(:/herryporco/img/harry-porco.png);",
            "image: url(:/cafe/img/cafe.gif);",
            "image: url(:/histograma/img/histograma.png);",
            "image: url(:/msword/img/ms_word.gif);",
            "image: url(:/musica/img/musica.jpg);",
            "image: url(:/viralata/img/vira-lara-caramelo.jpg);",
            ]
        style_sheet = (
            "QFrame {"
            f"{tasks[value]}"
            "background-repeat: no-repeat;"
            "background-position: center;"
            "}"
            )
        self.result_process.setStyleSheet(style_sheet)

    def progress_bar_value(self, value):
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

    def init_app_fifo(self):
        self.progress_bar_value([0, "136, 138, 133"])
        self.label_cpu_percentage.setText("0%")
        self.result_process.setStyleSheet("")
        queue_process_label = [self.label_p1, self.label_p2, self.label_p3]
        queue_process_frame = [self.queue_p1, self.queue_p2, self.queue_p3]
        for i in range(3):
            queue_process_label[i].setText("")
            queue_process_frame[i].setStyleSheet("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
