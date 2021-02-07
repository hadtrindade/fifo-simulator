from PySide2.QtCore import QThread, QObject, Signal, Slot


class SignalsToWorker(QObject):
    list_process = Signal(object)
    progress_signal = Signal(object)
    progress_signal_percentage = Signal(object)
    result_output = Signal(object)


class Worker(QThread):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signal = SignalsToWorker()

        self.kwargs["progress_signal"] = self.signal.progress_signal
        self.kwargs["result_output"] = self.signal.result_output
        self.kwargs[
            "progress_signal_percentage"
        ] = self.signal.progress_signal_percentage
        self.kwargs["list_process"] = self.signal.list_process

    @Slot()
    def stop(self):
        self.terminate()

    @Slot()
    def run(self):
        self.func(*self.args, **self.kwargs)
