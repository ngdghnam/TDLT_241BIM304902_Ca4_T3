from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.ptb2Widget import Ui_ptb2_window  
import sys
import math 

class Ptb2_Window(QMainWindow, Ui_ptb2_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Giải Phương trình bậc 2")

        self.button_giai.clicked.connect(self.Giai_ptb2)

    @Slot()
    def Giai_ptb2(self):
        try:
            a = float(self.textBrowser_hs1.text())
            b = float(self.textBrowser_hs2.text())
            c = float(self.textBrowser_hs3.text())

            if a == 0:
                if b == 0 and c == 0:
                    self.textBrowser_ketqua.setText(f"Phương trình có vô số nghiệm")
                elif b==0 and c != 0:
                    self.textBrowser_ketqua.setText("Phương trình vô nghiệm")
                else:
                    result = (-c) / b
                    self.textBrowser_ketqua.setText(f"{result}")
            else:
                delta = -b**2 - (4*a*c)
                if delta == 0:
                    x = (-b)/(2*a) 
                    self.textBrowser_ketqua.setText(f"Nghiệm kép: x = {x}")
                elif delta < 0: 
                    self.textBrowser_ketqua.setText("Phuong trinh vo nghiem")
                else: 
                    x1 = (-b - math.sqrt(delta))/(2*a)
                    x2 = (-b + math.sqrt(delta))/(2*a)
                    self.textBrowser_ketqua.setText(f"2 nghiệm phân biệt: x1 = {x1} - x2 = {x2}")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ptb2_Window()
    window.show()
    sys.exit(app.exec())
