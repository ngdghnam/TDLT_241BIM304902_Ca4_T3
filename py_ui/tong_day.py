# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tongDay.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Summation_Widget(object):
    def setupUi(self, Summation_Widget):
        if not Summation_Widget.objectName():
            Summation_Widget.setObjectName(u"Summation_Widget")
        Summation_Widget.resize(410, 205)
        self.input_start = QLineEdit(Summation_Widget)
        self.input_start.setObjectName(u"input_start")
        self.input_start.setGeometry(QRect(80, 10, 321, 31))
        font = QFont()
        font.setPointSize(10)
        self.input_start.setFont(font)
        self.input_start.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.label_2 = QLabel(Summation_Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 41, 20))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.textBrowser_ketqua = QTextBrowser(Summation_Widget)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(10, 110, 391, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.textBrowser_ketqua.setFont(font2)
        self.textBrowser_ketqua.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.button_giai = QPushButton(Summation_Widget)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(80, 160, 201, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")
        self.input_end = QLineEdit(Summation_Widget)
        self.input_end.setObjectName(u"input_end")
        self.input_end.setGeometry(QRect(80, 60, 321, 31))
        self.input_end.setFont(font)
        self.input_end.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.label = QLabel(Summation_Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 51, 31))
        self.label.setFont(font1)

        self.retranslateUi(Summation_Widget)

        QMetaObject.connectSlotsByName(Summation_Widget)
    # setupUi

    def retranslateUi(self, Summation_Widget):
        Summation_Widget.setWindowTitle(QCoreApplication.translate("Summation_Widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Summation_Widget", u"End", None))
        self.button_giai.setText(QCoreApplication.translate("Summation_Widget", u"T\u00ednh t\u1ed5ng d\u00e3y s\u1ed1", None))
        self.label.setText(QCoreApplication.translate("Summation_Widget", u"Start", None))
    # retranslateUi

