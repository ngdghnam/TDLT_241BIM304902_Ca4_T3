from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.to_hop import Ui_tohop_widget
import sys 
import math 

class Find_toHop(QMainWindow, Ui_tohop_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tính tổ hợp")

        self.button_giai.clicked.connect(self.Solve_toHop)

    @Slot()
    def Solve_toHop(self):
        try:
            n = int(self.input_N.text())
            k = int(self.input_K.text())
            if k > n: 
                self.textBrowser_ketqua.setText("Invalid")
            else:
                result = self.tinh(n, k)
                self.textBrowser_ketqua.setText(f"C({n}, {k}): {result}")
        except ValueError:
            self.textBrowser_ketqua.setText("Error: Invalid")

    @staticmethod
    def tinh(n, k):
        if k > n:
            return 'không tồn tại'  # Tổ hợp không tồn tại nếu k lớn hơn n
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
