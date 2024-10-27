# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lcm_widget.ui'
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

class Ui_LCM(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(425, 234)
        Form.setStyleSheet(u"color: white; \n"
"background-color: black")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 51, 21))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 51, 21))
        self.label_2.setFont(font)
        self.nhapSo_1 = QLineEdit(Form)
        self.nhapSo_1.setObjectName(u"nhapSo_1")
        self.nhapSo_1.setGeometry(QRect(90, 10, 321, 41))
        self.nhapSo_1.setStyleSheet(u"color: black;\n"
"background-color: white; ")
        self.nhapSo_2 = QLineEdit(Form)
        self.nhapSo_2.setObjectName(u"nhapSo_2")
        self.nhapSo_2.setGeometry(QRect(90, 70, 321, 41))
        self.nhapSo_2.setStyleSheet(u"color: black;\n"
"background-color: white; ")
        self.textBrowser_ketqua = QTextBrowser(Form)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(20, 130, 391, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.textBrowser_ketqua.setFont(font1)
        self.textBrowser_ketqua.setStyleSheet(u"color: black;\n"
"background-color: white; ")
        self.button_giai = QPushButton(Form)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(100, 190, 221, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"S\u1ed1 1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"S\u1ed1 2", None))
        self.button_giai.setText(QCoreApplication.translate("Form", u"T\u00ecm B\u1ed9i chung nh\u1ecf nh\u1ea5t", None))
    # retranslateUi

