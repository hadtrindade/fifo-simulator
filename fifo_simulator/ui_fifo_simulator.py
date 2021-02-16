# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fifo_simulator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resourses_rc

class Ui_FifoSimulator(object):
    def setupUi(self, FifoSimulator):
        if not FifoSimulator.objectName():
            FifoSimulator.setObjectName(u"FifoSimulator")
        FifoSimulator.resize(800, 600)
        FifoSimulator.setMinimumSize(QSize(800, 600))
        FifoSimulator.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(FifoSimulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 0, 800, 600))
        self.main_frame.setMinimumSize(QSize(800, 600))
        self.main_frame.setMaximumSize(QSize(800, 600))
        self.main_frame.setStyleSheet(u"background-color: rgb(235, 235, 241);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.body_frame = QFrame(self.main_frame)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setMinimumSize(QSize(800, 450))
        self.body_frame.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.body_frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(230, 20, 340, 51))
        self.label_title.setStyleSheet(u"background-color: none;\n"
"")
        self.circular_progress_bar_base = QFrame(self.body_frame)
        self.circular_progress_bar_base.setObjectName(u"circular_progress_bar_base")
        self.circular_progress_bar_base.setGeometry(QRect(10, 90, 320, 320))
        self.circular_progress_bar_base.setStyleSheet(u"")
        self.circular_progress_bar_base.setFrameShape(QFrame.NoFrame)
        self.circular_progress_bar_base.setFrameShadow(QFrame.Raised)
        self.circular_progress = QFrame(self.circular_progress_bar_base)
        self.circular_progress.setObjectName(u"circular_progress")
        self.circular_progress.setGeometry(QRect(10, 10, 300, 300))
        self.circular_progress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(211, 215, 207, 0), stop:0.75 rgba(136, 138, 133, 255));\n"
"}")
        self.circular_progress.setFrameShape(QFrame.StyledPanel)
        self.circular_progress.setFrameShadow(QFrame.Raised)
        self.circular_bg = QFrame(self.circular_progress_bar_base)
        self.circular_bg.setObjectName(u"circular_bg")
        self.circular_bg.setGeometry(QRect(10, 10, 300, 300))
        self.circular_bg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	\n"
"	background-color: rgba(211, 215, 207,120);\n"
"}")
        self.circular_bg.setFrameShape(QFrame.NoFrame)
        self.circular_bg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circular_progress_bar_base)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame {\n"
"	border-radius: 135px;\n"
"	background-color: rgb(211, 215, 207);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.label_cpu = QLabel(self.container)
        self.label_cpu.setObjectName(u"label_cpu")
        self.label_cpu.setGeometry(QRect(100, 40, 71, 41))
        font = QFont()
        font.setPointSize(25)
        self.label_cpu.setFont(font)
        self.label_cpu.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	font-size: 25pt;\n"
"	color: rgb(85, 87, 83);\n"
"}")
        self.label_cpu.setAlignment(Qt.AlignCenter)
        self.label_cpu_percentage = QLabel(self.container)
        self.label_cpu_percentage.setObjectName(u"label_cpu_percentage")
        self.label_cpu_percentage.setGeometry(QRect(70, 100, 121, 81))
        font1 = QFont()
        font1.setPointSize(40)
        self.label_cpu_percentage.setFont(font1)
        self.label_cpu_percentage.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	font-size: 40pt;\n"
"	color: rgb(85, 87, 83);\n"
"}\n"
"")
        self.label_cpu_percentage.setAlignment(Qt.AlignCenter)
        self.circular_bg.raise_()
        self.circular_progress.raise_()
        self.container.raise_()
        self.label_queue = QLabel(self.body_frame)
        self.label_queue.setObjectName(u"label_queue")
        self.label_queue.setGeometry(QRect(380, 150, 151, 21))
        self.button_start_stop = QPushButton(self.body_frame)
        self.button_start_stop.setObjectName(u"button_start_stop")
        self.button_start_stop.setGeometry(QRect(10, 10, 89, 25))
        self.button_start_stop.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(235, 240, 243);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	background-position: center;\n"
"	background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid  rgb(235, 240, 243);\n"
"	\n"
"	background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(69, 69, 69);\n"
"	background-color: rgb(217, 237, 247);\n"
"}")
        self.frame = QFrame(self.body_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(370, 330, 381, 77))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_in_exec = QLabel(self.frame)
        self.label_in_exec.setObjectName(u"label_in_exec")

        self.horizontalLayout.addWidget(self.label_in_exec)

        self.label_in_exec_p = QLabel(self.frame)
        self.label_in_exec_p.setObjectName(u"label_in_exec_p")

        self.horizontalLayout.addWidget(self.label_in_exec_p)

        self.label_ready = QLabel(self.frame)
        self.label_ready.setObjectName(u"label_ready")

        self.horizontalLayout.addWidget(self.label_ready)

        self.label_ready_p = QLabel(self.frame)
        self.label_ready_p.setObjectName(u"label_ready_p")

        self.horizontalLayout.addWidget(self.label_ready_p)

        self.process_bar = QProgressBar(self.body_frame)
        self.process_bar.setObjectName(u"process_bar")
        self.process_bar.setGeometry(QRect(350, 200, 50, 100))
        self.process_bar.setStyleSheet(u"QProgressBar {\n"
"	color:  rgb(69, 69,69);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	border-style: none;\n"
"	background-position: center;\n"
"	text-align: center;\n"
"	background-color: rgb(115, 210, 22);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(238, 238, 236);\n"
"\n"
"}\n"
"")
        self.process_bar.setValue(30)
        self.process_bar.setTextVisible(False)
        self.process_bar.setOrientation(Qt.Vertical)
        self.process_bar.setInvertedAppearance(True)
        self.process_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.body_frame)

        self.stats_frame = QFrame(self.main_frame)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setStyleSheet(u"background-color: rgb(211, 215, 207);")
        self.stats_frame.setFrameShape(QFrame.NoFrame)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.label_team = QLabel(self.stats_frame)
        self.label_team.setObjectName(u"label_team")
        self.label_team.setGeometry(QRect(540, 10, 251, 131))
        self.group_box_cpu = QGroupBox(self.stats_frame)
        self.group_box_cpu.setObjectName(u"group_box_cpu")
        self.group_box_cpu.setGeometry(QRect(10, 10, 151, 121))
        self.group_box_cpu.setStyleSheet(u"QLabel {\n"
"	color: rgb(46, 52, 54);\n"
"}")
        self.lavel_cpu_time = QLabel(self.group_box_cpu)
        self.lavel_cpu_time.setObjectName(u"lavel_cpu_time")
        self.lavel_cpu_time.setGeometry(QRect(10, 30, 61, 16))
        self.label_cpu_idle = QLabel(self.group_box_cpu)
        self.label_cpu_idle.setObjectName(u"label_cpu_idle")
        self.label_cpu_idle.setGeometry(QRect(10, 50, 51, 16))
        self.label_cpu_busy = QLabel(self.group_box_cpu)
        self.label_cpu_busy.setObjectName(u"label_cpu_busy")
        self.label_cpu_busy.setGeometry(QRect(10, 70, 71, 16))
        self.cpu_time_value = QLabel(self.group_box_cpu)
        self.cpu_time_value.setObjectName(u"cpu_time_value")
        self.cpu_time_value.setGeometry(QRect(100, 30, 47, 13))
        self.cpu_idel_value = QLabel(self.group_box_cpu)
        self.cpu_idel_value.setObjectName(u"cpu_idel_value")
        self.cpu_idel_value.setGeometry(QRect(100, 50, 47, 13))
        self.cpu_basy_value = QLabel(self.group_box_cpu)
        self.cpu_basy_value.setObjectName(u"cpu_basy_value")
        self.cpu_basy_value.setGeometry(QRect(100, 70, 47, 13))
        self.group_box_wait = QGroupBox(self.stats_frame)
        self.group_box_wait.setObjectName(u"group_box_wait")
        self.group_box_wait.setGeometry(QRect(180, 10, 151, 121))
        self.group_box_wait.setStyleSheet(u"QLabel {\n"
"	\n"
"	color: rgb(46, 52, 54);\n"
"}")
        self.label_wait_avarage = QLabel(self.group_box_wait)
        self.label_wait_avarage.setObjectName(u"label_wait_avarage")
        self.label_wait_avarage.setGeometry(QRect(10, 50, 51, 16))
        self.label_wait_min = QLabel(self.group_box_wait)
        self.label_wait_min.setObjectName(u"label_wait_min")
        self.label_wait_min.setGeometry(QRect(10, 30, 61, 16))
        self.label_wait_max = QLabel(self.group_box_wait)
        self.label_wait_max.setObjectName(u"label_wait_max")
        self.label_wait_max.setGeometry(QRect(10, 70, 61, 16))
        self.wait_min = QLabel(self.group_box_wait)
        self.wait_min.setObjectName(u"wait_min")
        self.wait_min.setGeometry(QRect(90, 30, 47, 13))
        self.wait_max = QLabel(self.group_box_wait)
        self.wait_max.setObjectName(u"wait_max")
        self.wait_max.setGeometry(QRect(90, 70, 47, 13))
        self.wait_mean = QLabel(self.group_box_wait)
        self.wait_mean.setObjectName(u"wait_mean")
        self.wait_mean.setGeometry(QRect(90, 50, 47, 13))

        self.verticalLayout.addWidget(self.stats_frame)

        FifoSimulator.setCentralWidget(self.centralwidget)

        self.retranslateUi(FifoSimulator)

        QMetaObject.connectSlotsByName(FifoSimulator)
    # setupUi

    def retranslateUi(self, FifoSimulator):
        FifoSimulator.setWindowTitle(QCoreApplication.translate("FifoSimulator", u"FIFO Process Simulator", None))
        self.label_title.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#555753;\">FIFO Process Simulator</span></p></body></html>", None))
        self.label_cpu.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-weight:600; color:#555753;\">CPU </span></p></body></html>", None))
        self.label_cpu_percentage.setText(QCoreApplication.translate("FifoSimulator", u"0%", None))
        self.label_queue.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Fila de processos:</span></p></body></html>", None))
        self.button_start_stop.setText(QCoreApplication.translate("FifoSimulator", u"Start", None))
        self.label_in_exec.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#828282;\">Em Execu\u00e7\u00e3o: </span></p></body></html>", None))
        self.label_in_exec_p.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#828282;\">PX</span></p></body></html>", None))
        self.label_ready.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#828282;\">Pronto(Pr\u00f3ximo): </span></p></body></html>", None))
        self.label_ready_p.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#828282;\">PY</span></p></body></html>", None))
        self.label_team.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Team:</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Ivo H. Trindade Silva</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Lucas de Mendon\u00e7a Schneider</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Jomilson Franklin Ciriaco</span></p></body></html>", None))
        self.group_box_cpu.setTitle(QCoreApplication.translate("FifoSimulator", u"CPU", None))
        self.lavel_cpu_time.setText(QCoreApplication.translate("FifoSimulator", u"Tempo", None))
        self.label_cpu_idle.setText(QCoreApplication.translate("FifoSimulator", u"Ocioso", None))
        self.label_cpu_busy.setText(QCoreApplication.translate("FifoSimulator", u"Ocupado", None))
        self.cpu_time_value.setText(QCoreApplication.translate("FifoSimulator", u"xxxx", None))
        self.cpu_idel_value.setText(QCoreApplication.translate("FifoSimulator", u"xxxx", None))
        self.cpu_basy_value.setText(QCoreApplication.translate("FifoSimulator", u"xxxx", None))
        self.group_box_wait.setTitle(QCoreApplication.translate("FifoSimulator", u"Espera", None))
        self.label_wait_avarage.setText(QCoreApplication.translate("FifoSimulator", u"M\u00e9dio", None))
        self.label_wait_min.setText(QCoreApplication.translate("FifoSimulator", u"Minimo", None))
        self.label_wait_max.setText(QCoreApplication.translate("FifoSimulator", u"M\u00e1ximo", None))
        self.wait_min.setText(QCoreApplication.translate("FifoSimulator", u"xxxx", None))
        self.wait_max.setText(QCoreApplication.translate("FifoSimulator", u"xxxx", None))
        self.wait_mean.setText(QCoreApplication.translate("FifoSimulator", u"xxxx", None))
    # retranslateUi

