# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(400, 710)
        widget.setStyleSheet(u"background-color: black;")
        self.main_label = QLabel(widget)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(10, 70, 381, 61))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(28)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet(u"color: white;")
        self.main_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.main_label_2 = QLabel(widget)
        self.main_label_2.setObjectName(u"main_label_2")
        self.main_label_2.setGeometry(QRect(10, 10, 381, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.main_label_2.setFont(font1)
        self.main_label_2.setStyleSheet(u"color: white;")
        self.main_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 140, 381, 561))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_divide = QPushButton(self.gridLayoutWidget)
        self.button_divide.setObjectName(u"button_divide")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(17)
        self.button_divide.setFont(font2)
        self.button_divide.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_divide, 8, 3, 1, 1)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setFont(font2)
        self.button_1.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_1, 7, 0, 1, 1)

        self.button_thuasonguyento = QPushButton(self.gridLayoutWidget)
        self.button_thuasonguyento.setObjectName(u"button_thuasonguyento")
        self.button_thuasonguyento.setFont(font2)
        self.button_thuasonguyento.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_thuasonguyento, 1, 2, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setFont(font2)
        self.button_9.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_9, 5, 2, 1, 1)

        self.button_3 = QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setFont(font2)
        self.button_3.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_3, 7, 2, 1, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setFont(font2)
        self.button_8.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_8, 5, 1, 1, 1)

        self.button_abs = QPushButton(self.gridLayoutWidget)
        self.button_abs.setObjectName(u"button_abs")
        self.button_abs.setFont(font2)
        self.button_abs.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_abs, 1, 3, 1, 1)

        self.button_pow = QPushButton(self.gridLayoutWidget)
        self.button_pow.setObjectName(u"button_pow")
        self.button_pow.setFont(font2)
        self.button_pow.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_pow, 4, 2, 1, 1)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setFont(font2)
        self.button_2.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_2, 7, 1, 1, 1)

        self.button_dot = QPushButton(self.gridLayoutWidget)
        self.button_dot.setObjectName(u"button_dot")
        self.button_dot.setFont(font2)
        self.button_dot.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_dot, 8, 2, 1, 1)

        self.button_factor = QPushButton(self.gridLayoutWidget)
        self.button_factor.setObjectName(u"button_factor")
        self.button_factor.setFont(font2)
        self.button_factor.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_factor, 2, 0, 1, 1)

        self.button_gcd = QPushButton(self.gridLayoutWidget)
        self.button_gcd.setObjectName(u"button_gcd")
        self.button_gcd.setFont(font2)
        self.button_gcd.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_gcd, 4, 0, 1, 1)

        self.button_tan = QPushButton(self.gridLayoutWidget)
        self.button_tan.setObjectName(u"button_tan")
        self.button_tan.setFont(font2)
        self.button_tan.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_tan, 3, 3, 1, 1)

        self.button_ptb2 = QPushButton(self.gridLayoutWidget)
        self.button_ptb2.setObjectName(u"button_ptb2")
        self.button_ptb2.setFont(font2)
        self.button_ptb2.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_ptb2, 2, 2, 1, 1)

        self.button_minus = QPushButton(self.gridLayoutWidget)
        self.button_minus.setObjectName(u"button_minus")
        self.button_minus.setFont(font2)
        self.button_minus.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_minus, 6, 3, 1, 1)

        self.button_multiply = QPushButton(self.gridLayoutWidget)
        self.button_multiply.setObjectName(u"button_multiply")
        self.button_multiply.setFont(font2)
        self.button_multiply.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_multiply, 7, 3, 1, 1)

        self.button_cos = QPushButton(self.gridLayoutWidget)
        self.button_cos.setObjectName(u"button_cos")
        self.button_cos.setFont(font2)
        self.button_cos.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_cos, 3, 2, 1, 1)

        self.button_lcm = QPushButton(self.gridLayoutWidget)
        self.button_lcm.setObjectName(u"button_lcm")
        self.button_lcm.setFont(font2)
        self.button_lcm.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_lcm, 4, 1, 1, 1)

        self.button_equal = QPushButton(self.gridLayoutWidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setFont(font2)
        self.button_equal.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_equal, 9, 2, 1, 2)

        self.button_ptb1 = QPushButton(self.gridLayoutWidget)
        self.button_ptb1.setObjectName(u"button_ptb1")
        self.button_ptb1.setFont(font2)
        self.button_ptb1.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_ptb1, 2, 1, 1, 1)

        self.button_to_hop = QPushButton(self.gridLayoutWidget)
        self.button_to_hop.setObjectName(u"button_to_hop")
        self.button_to_hop.setFont(font2)
        self.button_to_hop.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_to_hop, 1, 0, 1, 1)

        self.button_6 = QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setFont(font2)
        self.button_6.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_6, 6, 2, 1, 1)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setFont(font2)
        self.button_0.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_0, 8, 0, 1, 2)

        self.button_del = QPushButton(self.gridLayoutWidget)
        self.button_del.setObjectName(u"button_del")
        self.button_del.setFont(font2)
        self.button_del.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_del, 9, 0, 1, 2)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setFont(font2)
        self.button_4.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_4, 6, 0, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setFont(font2)
        self.button_5.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_5, 6, 1, 1, 1)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setFont(font2)
        self.button_plus.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_plus, 5, 3, 1, 1)

        self.button_7 = QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setFont(font2)
        self.button_7.setStyleSheet(u"background-color: #2A322E;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_7, 5, 0, 1, 1)

        self.button_sin = QPushButton(self.gridLayoutWidget)
        self.button_sin.setObjectName(u"button_sin")
        self.button_sin.setFont(font2)
        self.button_sin.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_sin, 3, 1, 1, 1)

        self.button_ptb3 = QPushButton(self.gridLayoutWidget)
        self.button_ptb3.setObjectName(u"button_ptb3")
        self.button_ptb3.setFont(font2)
        self.button_ptb3.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_ptb3, 2, 3, 1, 1)

        self.button_log = QPushButton(self.gridLayoutWidget)
        self.button_log.setObjectName(u"button_log")
        self.button_log.setFont(font2)
        self.button_log.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_log, 3, 0, 1, 1)

        self.button_pi = QPushButton(self.gridLayoutWidget)
        self.button_pi.setObjectName(u"button_pi")
        self.button_pi.setFont(font2)
        self.button_pi.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_pi, 4, 3, 1, 1)

        self.button_abs_2 = QPushButton(self.gridLayoutWidget)
        self.button_abs_2.setObjectName(u"button_abs_2")
        self.button_abs_2.setFont(font2)
        self.button_abs_2.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_abs_2, 0, 0, 1, 1)

        self.button_e = QPushButton(self.gridLayoutWidget)
        self.button_e.setObjectName(u"button_e")
        self.button_e.setFont(font2)
        self.button_e.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_e, 0, 1, 1, 1)

        self.button_chinh_hop = QPushButton(self.gridLayoutWidget)
        self.button_chinh_hop.setObjectName(u"button_chinh_hop")
        self.button_chinh_hop.setFont(font2)
        self.button_chinh_hop.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_chinh_hop, 1, 1, 1, 1)

        self.button_hoanvi = QPushButton(self.gridLayoutWidget)
        self.button_hoanvi.setObjectName(u"button_hoanvi")
        self.button_hoanvi.setFont(font2)
        self.button_hoanvi.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_hoanvi, 0, 2, 1, 1)

        self.button_sum = QPushButton(self.gridLayoutWidget)
        self.button_sum.setObjectName(u"button_sum")
        self.button_sum.setFont(font2)
        self.button_sum.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_sum, 0, 3, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"mainWindow", None))
        self.main_label.setText(QCoreApplication.translate("widget", u"0", None))
        self.main_label_2.setText(QCoreApplication.translate("widget", u"0", None))
        self.button_divide.setText(QCoreApplication.translate("widget", u"/", None))
        self.button_1.setText(QCoreApplication.translate("widget", u"1", None))
        self.button_thuasonguyento.setText(QCoreApplication.translate("widget", u"TSNT", None))
        self.button_9.setText(QCoreApplication.translate("widget", u"9", None))
        self.button_3.setText(QCoreApplication.translate("widget", u"3", None))
        self.button_8.setText(QCoreApplication.translate("widget", u"8", None))
        self.button_abs.setText(QCoreApplication.translate("widget", u"abs", None))
        self.button_pow.setText(QCoreApplication.translate("widget", u"**", None))
        self.button_2.setText(QCoreApplication.translate("widget", u"2", None))
        self.button_dot.setText(QCoreApplication.translate("widget", u".", None))
        self.button_factor.setText(QCoreApplication.translate("widget", u"Factor", None))
        self.button_gcd.setText(QCoreApplication.translate("widget", u"GCD", None))
        self.button_tan.setText(QCoreApplication.translate("widget", u"tan", None))
        self.button_ptb2.setText(QCoreApplication.translate("widget", u"PTB2", None))
        self.button_minus.setText(QCoreApplication.translate("widget", u"-", None))
        self.button_multiply.setText(QCoreApplication.translate("widget", u"*", None))
        self.button_cos.setText(QCoreApplication.translate("widget", u"cos", None))
        self.button_lcm.setText(QCoreApplication.translate("widget", u"LCM", None))
        self.button_equal.setText(QCoreApplication.translate("widget", u"=", None))
        self.button_ptb1.setText(QCoreApplication.translate("widget", u"PTB1", None))
        self.button_to_hop.setText(QCoreApplication.translate("widget", u"C", None))
        self.button_6.setText(QCoreApplication.translate("widget", u"6", None))
        self.button_0.setText(QCoreApplication.translate("widget", u"0", None))
        self.button_del.setText(QCoreApplication.translate("widget", u"DEL", None))
        self.button_4.setText(QCoreApplication.translate("widget", u"4", None))
        self.button_5.setText(QCoreApplication.translate("widget", u"5", None))
        self.button_plus.setText(QCoreApplication.translate("widget", u"+", None))
        self.button_7.setText(QCoreApplication.translate("widget", u"7", None))
        self.button_sin.setText(QCoreApplication.translate("widget", u"sin", None))
        self.button_ptb3.setText(QCoreApplication.translate("widget", u"PTB3", None))
        self.button_log.setText(QCoreApplication.translate("widget", u"log", None))
        self.button_pi.setText(QCoreApplication.translate("widget", u"cotan", None))
        self.button_abs_2.setText(QCoreApplication.translate("widget", u"SQRT", None))
        self.button_e.setText(QCoreApplication.translate("widget", u"BIN", None))
        self.button_chinh_hop.setText(QCoreApplication.translate("widget", u"A", None))
        self.button_hoanvi.setText(QCoreApplication.translate("widget", u"HVi", None))
        self.button_sum.setText(QCoreApplication.translate("widget", u"Sum", None))
    # retranslateUi

