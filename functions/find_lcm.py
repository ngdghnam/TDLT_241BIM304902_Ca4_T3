from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.lcm import Ui_LCM
import math 

class Lcm_Window(QMainWindow, Ui_LCM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tìm bội chung nhỏ nhất")

        self.button_giai.clicked.connect(self.Find_lcm)

    @Slot()
    def Find_lcm(self):
        try: 
            num_1 = int(self.nhapSo_1.text())
            num_2 = int(self.nhapSo_2.text())
            result = math.lcm(num_1, num_2)
            self.textBrowser_ketqua.setText(f"Bội chung nhỏ nhất: {result}")
        except ValueError:
            QMessageBox.warning(self, "Invalid")