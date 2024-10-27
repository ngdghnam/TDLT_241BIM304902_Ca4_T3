# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gcd_widget.ui'
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

class Ui_gcd_widget(object):
    def setupUi(self, gcd_widget):
        if not gcd_widget.objectName():
            gcd_widget.setObjectName(u"gcd_widget")
        gcd_widget.resize(424, 240)
        gcd_widget.setStyleSheet(u"color: white;\n"
"background-color: black;")
        self.label_1 = QLabel(gcd_widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 30, 51, 31))
        font = QFont()
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.nhapSo_1 = QLineEdit(gcd_widget)
        self.nhapSo_1.setObjectName(u"nhapSo_1")
        self.nhapSo_1.setGeometry(QRect(70, 20, 341, 41))
        self.nhapSo_1.setStyleSheet(u"background-color: white; \n"
"color: black;")
        self.label_2 = QLabel(gcd_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 51, 31))
        self.label_2.setFont(font)
        self.nhapSo_2 = QLineEdit(gcd_widget)
        self.nhapSo_2.setObjectName(u"nhapSo_2")
        self.nhapSo_2.setGeometry(QRect(70, 80, 341, 41))
        self.nhapSo_2.setStyleSheet(u"background-color: white; \n"
"color: black;")
        self.button_giai = QPushButton(gcd_widget)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(110, 200, 211, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")
        self.textBrowser_ketqua = QTextBrowser(gcd_widget)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(10, 140, 401, 41))
        self.textBrowser_ketqua.setStyleSheet(u"color: black; \n"
"background-color: white;")

        self.retranslateUi(gcd_widget)

        QMetaObject.connectSlotsByName(gcd_widget)
    # setupUi

    def retranslateUi(self, gcd_widget):
        gcd_widget.setWindowTitle(QCoreApplication.translate("gcd_widget", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("gcd_widget", u"S\u1ed1 1", None))
        self.label_2.setText(QCoreApplication.translate("gcd_widget", u"S\u1ed1 2", None))
        self.button_giai.setText(QCoreApplication.translate("gcd_widget", u"T\u00ecm \u01af\u1edbc chung l\u1edbn nh\u1ea5t", None))
    # retranslateUi

