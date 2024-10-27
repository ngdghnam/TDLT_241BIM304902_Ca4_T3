# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pag3_ptb2.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextBrowser, QWidget, QLineEdit)

class Ui_ptb2_window(object):
    def setupUi(self, ptb2_window):
        if not ptb2_window.objectName():
            ptb2_window.setObjectName(u"ptb2_window")
        ptb2_window.resize(430, 248)
        ptb2_window.setStyleSheet(u"color: white;\n"
"background-color: black;")
        self.label_hs1 = QLabel(ptb2_window)
        self.label_hs1.setObjectName(u"label_hs1")
        self.label_hs1.setGeometry(QRect(10, 10, 71, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_hs1.setFont(font)
        self.textBrowser_hs1 = QLineEdit(ptb2_window)
        self.textBrowser_hs1.setObjectName(u"textBrowser_hs1")
        self.textBrowser_hs1.setGeometry(QRect(90, 10, 331, 31))
        self.textBrowser_hs1.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_hs2 = QLabel(ptb2_window)
        self.label_hs2.setObjectName(u"label_hs2")
        self.label_hs2.setGeometry(QRect(10, 60, 71, 31))
        self.label_hs2.setFont(font)
        self.textBrowser_hs2 = QLineEdit(ptb2_window)
        self.textBrowser_hs2.setObjectName(u"textBrowser_hs2")
        self.textBrowser_hs2.setGeometry(QRect(90, 60, 331, 31))
        self.textBrowser_hs2.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_hs3 = QLabel(ptb2_window)
        self.label_hs3.setObjectName(u"label_hs3")
        self.label_hs3.setGeometry(QRect(10, 110, 71, 31))
        self.label_hs3.setFont(font)
        self.textBrowser_hs3 = QLineEdit(ptb2_window)
        self.textBrowser_hs3.setObjectName(u"textBrowser_hs3")
        self.textBrowser_hs3.setGeometry(QRect(90, 110, 331, 31))
        self.textBrowser_hs3.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_ketqua = QLabel(ptb2_window)
        self.label_ketqua.setObjectName(u"label_ketqua")
        self.label_ketqua.setGeometry(QRect(10, 160, 71, 31))
        self.label_ketqua.setFont(font)
        self.textBrowser_ketqua = QLineEdit(ptb2_window)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(90, 160, 331, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.textBrowser_ketqua.setFont(font1)
        self.textBrowser_ketqua.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.button_giai = QPushButton(ptb2_window)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(140, 210, 151, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.retranslateUi(ptb2_window)

        QMetaObject.connectSlotsByName(ptb2_window)
    # setupUi

    def retranslateUi(self, ptb2_window):
        ptb2_window.setWindowTitle(QCoreApplication.translate("ptb2_window", u"ptb3Window", None))
        self.label_hs1.setText(QCoreApplication.translate("ptb2_window", u"H\u1ec7 s\u1ed1 1", None))
        self.label_hs2.setText(QCoreApplication.translate("ptb2_window", u"H\u1ec7 s\u1ed1 2", None))
        self.label_hs3.setText(QCoreApplication.translate("ptb2_window", u"H\u1ec7 s\u1ed1 3", None))
        self.label_ketqua.setText(QCoreApplication.translate("ptb2_window", u"K\u1ebft qu\u1ea3", None))
        self.button_giai.setText(QCoreApplication.translate("ptb2_window", u"Gi\u1ea3i Ph\u01b0\u01a1ng tr\u00ecnh b\u1eadc 2", None))
    # retranslateUi

