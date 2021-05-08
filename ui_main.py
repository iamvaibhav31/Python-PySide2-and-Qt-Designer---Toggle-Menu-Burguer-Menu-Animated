# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainIbuJgU.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 513)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"font: 8pt \"Century Gothic\";\n"
"background-color: rgb(170, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setAutoFillBackground(False)
        self.btn_toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar)

        self.contant = QFrame(self.centralwidget)
        self.contant.setObjectName(u"contant")
        self.contant.setFrameShape(QFrame.NoFrame)
        self.contant.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contant)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.contant)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_top_menus.sizePolicy().hasHeightForWidth())
        self.frame_top_menus.setSizePolicy(sizePolicy1)
        self.frame_top_menus.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_top_menus.setFocusPolicy(Qt.WheelFocus)
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_top_menus)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 8pt \"Century Gothic\";	\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 85, 255);\n"
"	font: 8pt \"Century Gothic\";\n"
"	background-color: rgb(170, 170, 255);\n"
"	border: 0px solid;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_top_menus)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 8pt \"Century Gothic\";	\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 85, 255);\n"
"	font: 8pt \"Century Gothic\";\n"
"	background-color: rgb(170, 170, 255);\n"
"	border: 0px solid;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.frame_top_menus)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.contant)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.page_widget = QStackedWidget(self.frame_pages)
        self.page_widget.setObjectName(u"page_widget")
        self.page_widget.setGeometry(QRect(0, 0, 931, 471))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_widget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.contant)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu_1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Menu_2", None))
    # retranslateUi

