import sys
from PySide2 import QtWidgets
from ui_fifo_simulator import Ui_FifoSimulator


class MainWindow(QtWidgets.QMainWindow, Ui_FifoSimulator):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
