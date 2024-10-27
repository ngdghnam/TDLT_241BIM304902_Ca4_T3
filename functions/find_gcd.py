from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.gcd import Ui_gcd_widget
import sys 
import math 

class Gcd_Window(QMainWindow, Ui_gcd_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tìm ước chung lớn nhất")

        self.button_giai.clicked.connect(self.Find_gcd)

    @Slot()
    def Find_gcd(self):
        try: 
            num_1 = int(self.nhapSo_1.text())
            num_2 = int(self.nhapSo_2.text())
            result = math.gcd(num_1, num_2)
            self.textBrowser_ketqua.setText(f"Ước chung lớn nhất: {result}")
        except ValueError:
            QMessageBox.warning(self, "Invalid")
