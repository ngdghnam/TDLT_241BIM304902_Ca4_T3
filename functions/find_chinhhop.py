from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.chinh_hop import Ui_chinh_hop_Widget
import math 

class Find_chinhHop(QMainWindow, Ui_chinh_hop_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tính chỉnh hợp")

        self.button_giai.clicked.connect(self.Solve_chinhHop)
    
    @Slot()
    def Solve_chinhHop(self):
        try:
            n = int(self.input_N.text())
            k = int(self.input_K.text())
            if k > n: 
                self.textBrowser_ketqua.setText("Invalid")
            else:
                result = self.tinh(n, k)
                self.textBrowser_ketqua.setText(f"A({n}, {k}): {result}")
        except ValueError:
            self.textBrowser_ketqua.setText("Error: Invalid")

    @staticmethod
    def tinh(n, k):
        if k > n:
            return "Không tồn tại"
        return math.factorial(n) // math.factorial(n-k)