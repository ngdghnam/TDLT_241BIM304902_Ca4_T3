# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,QLineEdit,
    QTextBrowser, QWidget)

class Ui_ptb1_window(object):
    def setupUi(self, ptb1_window):
        if not ptb1_window.objectName():
            ptb1_window.setObjectName(u"ptb1_window")
        ptb1_window.resize(426, 207)
        ptb1_window.setStyleSheet(u"background-color: black; \n"
"color: white; ")
        self.label_hs1 = QLabel(ptb1_window)
        self.label_hs1.setObjectName(u"label_hs1")
        self.label_hs1.setGeometry(QRect(10, 20, 71, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_hs1.setFont(font)
        self.textBrowser_hs1 = QLineEdit(ptb1_window)
        self.textBrowser_hs1.setObjectName(u"textBrowser_hs1")
        self.textBrowser_hs1.setGeometry(QRect(90, 20, 331, 31))
        self.textBrowser_hs1.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.label_hs2 = QLabel(ptb1_window)
        self.label_hs2.setObjectName(u"label_hs2")
        self.label_hs2.setGeometry(QRect(10, 70, 71, 31))
        self.label_hs2.setFont(font)
        self.textBrowser_hs2 = QLineEdit(ptb1_window)
        self.textBrowser_hs2.setObjectName(u"textBrowser_hs2")
        self.textBrowser_hs2.setGeometry(QRect(90, 70, 331, 31))
        self.textBrowser_hs2.setStyleSheet(u"color: black; \n"
"background-color: white; ")
        self.button_giai = QPushButton(ptb1_window)
        self.button_giai.setObjectName(u"button_giai")
        self.button_giai.setGeometry(QRect(140, 170, 151, 28))
        self.button_giai.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")
        self.label_ketqua = QLabel(ptb1_window)
        self.label_ketqua.setObjectName(u"label_ketqua")
        self.label_ketqua.setGeometry(QRect(10, 120, 71, 31))
        self.label_ketqua.setFont(font)
        self.textBrowser_ketqua = QLineEdit(ptb1_window)
        self.textBrowser_ketqua.setObjectName(u"textBrowser_ketqua")
        self.textBrowser_ketqua.setGeometry(QRect(90, 120, 331, 31))
        self.textBrowser_ketqua.setStyleSheet(u"color: black; \n"
"background-color: white; ")

        self.retranslateUi(ptb1_window)

        QMetaObject.connectSlotsByName(ptb1_window)
    # setupUi

    def retranslateUi(self, ptb1_window):
        ptb1_window.setWindowTitle(QCoreApplication.translate("ptb1_window", u"ptb1Window", None))
        self.label_hs1.setText(QCoreApplication.translate("ptb1_window", u"H\u1ec7 s\u1ed1 1", None))
        self.label_hs2.setText(QCoreApplication.translate("ptb1_window", u"H\u1ec7 s\u1ed1 2", None))
        self.button_giai.setText(QCoreApplication.translate("ptb1_window", u"Gi\u1ea3i Ph\u01b0\u01a1ng tr\u00ecnh b\u1eadc 1", None))
        self.label_ketqua.setText(QCoreApplication.translate("ptb1_window", u"K\u1ebft qu\u1ea3", None))
    # retranslateUi

