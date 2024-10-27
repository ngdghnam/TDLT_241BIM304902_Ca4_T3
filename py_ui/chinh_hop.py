# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chinh_hop.ui'
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

class Ui_chinh_hop_Widget(object):
    def setupUi(self, chinh_hop_Widget):
        if not chinh_hop_Widget.objectName():
            chinh_hop_Widget.setObjectName(u"chinh_hop_Widget")
        chinh_hop_Widget.resize(400, 214)
        self.label = QLabel(chinh_hop_Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 21, 16))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.input_N = QLineEdit(chinh_hop_Widget)
        self.input_N.setObjectName(u"input_N")
        self.input_N.setGeometry(QRect(60, 20, 321, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.input_N.setFont(font1)
        self.label_2 = QLabel(chinh_hop_Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 21, 16))
        self.label_2.setFont(font)
        self.input_K = QLineEdit(chinh_hop_Widget)
        self.input_K.setObjectName(u"input_K")
        self.input_K.setGeometry(QRect(60, 70, 321, 31))
        self.input_K.setFont(font1)
        self.textBrowser_ketqua = QTextBrowser(chinh_hop_Widget)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(30, 120, 351, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.textBrowser_ketqua.setFont(font2)
        self.button_giai = QPushButton(chinh_hop_Widget)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(100, 170, 201, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.retranslateUi(chinh_hop_Widget)

        QMetaObject.connectSlotsByName(chinh_hop_Widget)
    # setupUi

    def retranslateUi(self, chinh_hop_Widget):
        chinh_hop_Widget.setWindowTitle(QCoreApplication.translate("chinh_hop_Widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("chinh_hop_Widget", u"N", None))
        self.label_2.setText(QCoreApplication.translate("chinh_hop_Widget", u"K", None))
        self.button_giai.setText(QCoreApplication.translate("chinh_hop_Widget", u"T\u00ednh ch\u1ec9nh h\u1ee3p", None))
    # retranslateUi

