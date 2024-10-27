# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pag4_ptb3.ui'
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
    QLineEdit, QWidget)

class Ui_ptb3_window(object):
    def setupUi(self, ptb3_window):
        if not ptb3_window.objectName():
            ptb3_window.setObjectName(u"ptb3_window")
        ptb3_window.resize(429, 301)
        ptb3_window.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.button_giai = QPushButton(ptb3_window)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(140, 260, 151, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")
        self.textBrowser_hs1 = QLineEdit(ptb3_window)
        self.textBrowser_hs1.setObjectName(u"textBrowser_hs1")
        self.textBrowser_hs1.setGeometry(QRect(90, 10, 331, 31))
        self.textBrowser_hs1.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_hs2 = QLabel(ptb3_window)
        self.label_hs2.setObjectName(u"label_hs2")
        self.label_hs2.setGeometry(QRect(10, 60, 71, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_hs2.setFont(font)
        self.label_hs3 = QLabel(ptb3_window)
        self.label_hs3.setObjectName(u"label_hs3")
        self.label_hs3.setGeometry(QRect(10, 110, 71, 31))
        self.label_hs3.setFont(font)
        self.textBrowser_hs2 = QLineEdit(ptb3_window)
        self.textBrowser_hs2.setObjectName(u"textBrowser_hs2")
        self.textBrowser_hs2.setGeometry(QRect(90, 60, 331, 31))
        self.textBrowser_hs2.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_hs1 = QLabel(ptb3_window)
        self.label_hs1.setObjectName(u"label_hs1")
        self.label_hs1.setGeometry(QRect(10, 10, 71, 31))
        self.label_hs1.setFont(font)
        self.label_ketqua = QLabel(ptb3_window)
        self.label_ketqua.setObjectName(u"label_ketqua")
        self.label_ketqua.setGeometry(QRect(10, 210, 71, 31))
        self.label_ketqua.setFont(font)
        self.textBrowser_ketqua = QLineEdit(ptb3_window)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(90, 210, 331, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.textBrowser_ketqua.setFont(font1)
        self.textBrowser_ketqua.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.textBrowser_hs3 = QLineEdit(ptb3_window)
        self.textBrowser_hs3.setObjectName(u"textBrowser_hs3")
        self.textBrowser_hs3.setGeometry(QRect(90, 110, 331, 31))
        self.textBrowser_hs3.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_hs4 = QLabel(ptb3_window)
        self.label_hs4.setObjectName(u"label_hs4")
        self.label_hs4.setGeometry(QRect(10, 160, 71, 31))
        self.label_hs4.setFont(font)
        self.textBrowser_hs4 = QLineEdit(ptb3_window)
        self.textBrowser_hs4.setObjectName(u"textBrowser_hs4")
        self.textBrowser_hs4.setGeometry(QRect(90, 160, 331, 31))
        self.textBrowser_hs4.setFont(font1)
        self.textBrowser_hs4.setStyleSheet(u"color: black; \n"
"background-color: white; ")

        self.retranslateUi(ptb3_window)

        QMetaObject.connectSlotsByName(ptb3_window)
    # setupUi

    def retranslateUi(self, ptb3_window):
        ptb3_window.setWindowTitle(QCoreApplication.translate("ptb3_window", u"ptb2Window", None))
        self.button_giai.setText(QCoreApplication.translate("ptb3_window", u"Gi\u1ea3i Ph\u01b0\u01a1ng tr\u00ecnh b\u1eadc 3", None))
        self.label_hs2.setText(QCoreApplication.translate("ptb3_window", u"H\u1ec7 s\u1ed1 2", None))
        self.label_hs3.setText(QCoreApplication.translate("ptb3_window", u"H\u1ec7 s\u1ed1 3", None))
        self.label_hs1.setText(QCoreApplication.translate("ptb3_window", u"H\u1ec7 s\u1ed1 1", None))
        self.label_ketqua.setText(QCoreApplication.translate("ptb3_window", u"K\u1ebft qu\u1ea3", None))
        self.label_hs4.setText(QCoreApplication.translate("ptb3_window", u"H\u1ec7 s\u1ed1 4", None))
    # retranslateUi

