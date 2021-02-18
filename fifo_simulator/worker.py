from PySide2.QtCore import QThread, QObject, Signal, Slot


class SignalsToWorker(QObject):
    list_process = Signal(object)
    clock_signal = Signal(object)
    cpu_busy_signal = Signal(object)
    progress_signal = Signal(object)
    progress_signal_process = Signal(object)
    progress_signal_process_run = Signal(object)
    progress_signal_process_ready = Signal(object)
    progress_signal_percentage = Signal(object)


class Worker(QThread):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signal = SignalsToWorker()

        self.kwargs["progress_signal"] = self.signal.progress_signal
        self.kwargs[
            "progress_signal_process"
        ] = self.signal.progress_signal_process
        self.kwargs[
            "progress_signal_process_run"
        ] = self.signal.progress_signal_process_run
        self.kwargs[
            "progress_signal_process_ready"
        ] = self.signal.progress_signal_process_ready
        self.kwargs[
            "progress_signal_percentage"
        ] = self.signal.progress_signal_percentage
        self.kwargs["list_process"] = self.signal.list_process
        self.kwargs["clock_signal"] = self.signal.clock_signal
        self.kwargs["cpu_busy_signal"] = self.signal.cpu_busy_signal

    @Slot()
    def stop(self):
        self.terminate()

    @Slot()
    def run(self):
        self.func(*self.args, **self.kwargs)
