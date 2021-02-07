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
        self.body_frame.setStyleSheet(u"")
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.body_frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(230, 20, 340, 51))
        self.label_title.setStyleSheet(u"background-color: none;\n"
"")
        self.circular_progress_bar_base = QFrame(self.body_frame)
        self.circular_progress_bar_base.setObjectName(u"circular_progress_bar_base")
        self.circular_progress_bar_base.setGeometry(QRect(160, 90, 320, 320))
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
        self.label_cpu.setGeometry(QRect(100, 40, 67, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_cpu.setFont(font)
        self.label_cpu.setStyleSheet(u"background-color: none;")
        self.label_cpu.setAlignment(Qt.AlignCenter)
        self.label_cpu_percentage = QLabel(self.container)
        self.label_cpu_percentage.setObjectName(u"label_cpu_percentage")
        self.label_cpu_percentage.setGeometry(QRect(90, 110, 81, 61))
        self.label_cpu_percentage.setFont(font)
        self.label_cpu_percentage.setStyleSheet(u"background-color: none;")
        self.label_cpu_percentage.setAlignment(Qt.AlignCenter)
        self.circular_bg.raise_()
        self.circular_progress.raise_()
        self.container.raise_()
        self.queue_p1 = QFrame(self.body_frame)
        self.queue_p1.setObjectName(u"queue_p1")
        self.queue_p1.setGeometry(QRect(490, 210, 81, 71))
        self.queue_p1.setStyleSheet(u"")
        self.queue_p1.setFrameShape(QFrame.NoFrame)
        self.queue_p1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.queue_p1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_p1 = QLabel(self.queue_p1)
        self.label_p1.setObjectName(u"label_p1")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_p1.setFont(font1)
        self.label_p1.setStyleSheet(u"QLabel{\n"
"	color: rgb(85, 87, 83);\n"
"	background-color: none;\n"
"}")
        self.label_p1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_p1)

        self.result_process = QFrame(self.body_frame)
        self.result_process.setObjectName(u"result_process")
        self.result_process.setGeometry(QRect(10, 190, 141, 121))
        self.result_process.setStyleSheet(u"background-color: rgb(114, 159, 207);\n"
"background-image: url(:/folder/img/cil-folder.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.result_process.setFrameShape(QFrame.NoFrame)
        self.result_process.setFrameShadow(QFrame.Raised)
        self.label_queue = QLabel(self.body_frame)
        self.label_queue.setObjectName(u"label_queue")
        self.label_queue.setGeometry(QRect(550, 150, 151, 21))
        self.queue_p2 = QFrame(self.body_frame)
        self.queue_p2.setObjectName(u"queue_p2")
        self.queue_p2.setGeometry(QRect(590, 210, 81, 71))
        self.queue_p2.setStyleSheet(u"")
        self.queue_p2.setFrameShape(QFrame.NoFrame)
        self.queue_p2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.queue_p2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_p2 = QLabel(self.queue_p2)
        self.label_p2.setObjectName(u"label_p2")
        self.label_p2.setFont(font1)
        self.label_p2.setStyleSheet(u"QLabel{\n"
"	color: rgb(85, 87, 83);\n"
"	background-color: none;\n"
"}")
        self.label_p2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_p2)

        self.queue_p3 = QFrame(self.body_frame)
        self.queue_p3.setObjectName(u"queue_p3")
        self.queue_p3.setGeometry(QRect(690, 210, 81, 71))
        self.queue_p3.setStyleSheet(u"")
        self.queue_p3.setFrameShape(QFrame.NoFrame)
        self.queue_p3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.queue_p3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_p3 = QLabel(self.queue_p3)
        self.label_p3.setObjectName(u"label_p3")
        self.label_p3.setFont(font1)
        self.label_p3.setStyleSheet(u"QLabel{\n"
"	color: rgb(85, 87, 83);\n"
"	background-color: none;\n"
"}")
        self.label_p3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_p3)

        self.label_output = QLabel(self.body_frame)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setGeometry(QRect(0, 150, 151, 21))
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

        self.verticalLayout.addWidget(self.body_frame)

        self.stats_frame = QFrame(self.main_frame)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setStyleSheet(u"background-color: rgb(211, 215, 207);")
        self.stats_frame.setFrameShape(QFrame.NoFrame)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.label_stats = QLabel(self.stats_frame)
        self.label_stats.setObjectName(u"label_stats")
        self.label_stats.setGeometry(QRect(10, 10, 61, 21))
        self.label = QLabel(self.stats_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 221, 17))

        self.verticalLayout.addWidget(self.stats_frame)

        FifoSimulator.setCentralWidget(self.centralwidget)

        self.retranslateUi(FifoSimulator)

        QMetaObject.connectSlotsByName(FifoSimulator)
    # setupUi

    def retranslateUi(self, FifoSimulator):
        FifoSimulator.setWindowTitle(QCoreApplication.translate("FifoSimulator", u"FIFO Simulator Process", None))
        self.label_title.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#555753;\">FIFO Simalator Process</span></p></body></html>", None))
        self.label_cpu.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-weight:600; color:#555753;\">CPU </span></p></body></html>", None))
        self.label_cpu_percentage.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-size:36pt; color:#555753;\">0%</span></p></body></html>", None))
        self.label_p1.setText("")
        self.label_queue.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Fila de processos.</span></p></body></html>", None))
        self.label_p2.setText("")
        self.label_p3.setText("")
        self.label_output.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#555753;\">Saida</span></p></body></html>", None))
        self.button_start_stop.setText(QCoreApplication.translate("FifoSimulator", u"Start", None))
        self.label_stats.setText(QCoreApplication.translate("FifoSimulator", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#555753;\">Stats</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("FifoSimulator", u"By: Pau de dar em doido Team.", None))
    # retranslateUi

