# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toHop.ui'
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

class Ui_tohop_widget(object):
    def setupUi(self, tohop_widget):
        if not tohop_widget.objectName():
            tohop_widget.setObjectName(u"tohop_widget")
        tohop_widget.resize(367, 214)
        tohop_widget.setStyleSheet(u"color: white;\n"
"background-color: black;")
        self.input_K = QLineEdit(tohop_widget)
        self.input_K.setObjectName(u"input_K")
        self.input_K.setGeometry(QRect(40, 70, 321, 31))
        font = QFont()
        font.setPointSize(10)
        self.input_K.setFont(font)
        self.input_K.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.textBrowser_ketqua = QTextBrowser(tohop_widget)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(10, 120, 351, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.textBrowser_ketqua.setFont(font1)
        self.textBrowser_ketqua.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.label_2 = QLabel(tohop_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 21, 16))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label = QLabel(tohop_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 21, 16))
        self.label.setFont(font2)
        self.input_N = QLineEdit(tohop_widget)
        self.input_N.setObjectName(u"input_N")
        self.input_N.setGeometry(QRect(40, 20, 321, 31))
        self.input_N.setFont(font)
        self.input_N.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.button_giai = QPushButton(tohop_widget)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(80, 170, 201, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.retranslateUi(tohop_widget)

        QMetaObject.connectSlotsByName(tohop_widget)
    # setupUi

    def retranslateUi(self, tohop_widget):
        tohop_widget.setWindowTitle(QCoreApplication.translate("tohop_widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("tohop_widget", u"K", None))
        self.label.setText(QCoreApplication.translate("tohop_widget", u"N", None))
        self.button_giai.setText(QCoreApplication.translate("tohop_widget", u"T\u00ednh t\u1ed5 h\u1ee3p", None))
    # retranslateUi

