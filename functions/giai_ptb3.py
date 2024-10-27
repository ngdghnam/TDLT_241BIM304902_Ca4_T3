from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.ptb3Widget import Ui_ptb3_window
import sys
from math import cos, acos, sqrt, cbrt, pi

class Ptb3_Window(QMainWindow, Ui_ptb3_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_giai.clicked.connect(self.Giai_ptb3)
        self.setWindowTitle("Giải phương trình bậc 3")

    @Slot()
    def Giai_ptb3(self):
        try:
            # Get input values
            a = float(self.textBrowser_hs1.text())
            b = float(self.textBrowser_hs2.text())
            c = float(self.textBrowser_hs3.text())
            d = float(self.textBrowser_hs4.text())

            # Case: Third-degree polynomial (a ≠ 0)
            if a != 0:
                delta = b**2 - 3 * a * c
                k = ((9 * a * b * c) - (2 * b**3) - (27 * a**2 * d)) / (2 * sqrt(abs(delta)**3)) if delta != 0 else 0
                m = b**2 - 27 * a**2 * d

                if delta == 0:
                    if m == 0:
                        x = -b / (3 * a)
                        self.textBrowser_ketqua.setText(f"Phương trình có nghiệm bội: x = {x}")
                    else:
                        x = (-b + cbrt(m)) / (3 * a)
                        self.textBrowser_ketqua.setText(f"Phương trình có 1 nghiệm: x = {x}")
                elif delta < 0:
                    x = (sqrt(abs(delta)) / (3 * a)) * ((cbrt(k + sqrt(k**2 + 1))) + (cbrt(k - sqrt(k**2 + 1)))) - (b / (3 * a))
                    self.textBrowser_ketqua.setText(f"Phương trình có 1 nghiệm: x = {x}")
                else:
                    if abs(k) > 1:
                        x = ((sqrt(delta) * abs(k)) / (3 * a * k)) * ((cbrt(abs(k) + sqrt(k**2 - 1))) + (cbrt(abs(k) - sqrt(k**2 - 1)))) - (b / (3 * a))
                        self.textBrowser_ketqua.setText(f"Phương trình có 1 nghiệm: x = {x}")
                    else:
                        x1 = (2 * sqrt(delta) * cos(acos(k) / 3) - b) / (3 * a)
                        x2 = (2 * sqrt(delta) * cos((acos(k) / 3) - (2 * pi / 3)) - b) / (3 * a)
                        x3 = (2 * sqrt(delta) * cos((acos(k) / 3) + (2 * pi / 3)) - b) / (3 * a)
                        self.textBrowser_ketqua.setText(f"Phương trình có 3 nghiệm: x1 = {x1}, x2 = {x2}, x3 = {x3}")

            # Case: Second-degree polynomial or lower if a == 0
            else:
                # Check if it's a second-degree equation
                if b != 0:
                    delta = c**2 - 4 * b * d
                    if delta == 0:
                        x = -c / (2 * b)
                        self.textBrowser_ketqua.setText(f"Nghiệm kép: x = {x}")
                    elif delta < 0:
                        self.textBrowser_ketqua.setText("Phương trình vô nghiệm")
                    else:
                        x1 = (-c - sqrt(delta)) / (2 * b)
                        x2 = (-c + sqrt(delta)) / (2 * b)
                        self.textBrowser_ketqua.setText(f"2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
                # Linear equation if b == 0
                elif c != 0:
                    x = -d / c
                    self.textBrowser_ketqua.setText(f"Nghiệm của phương trình bậc nhất: x = {x}")
                else:
                    # Handle case for d == 0 as a special case with infinite solutions
                    if d == 0:
                        self.textBrowser_ketqua.setText("Phương trình có vô số nghiệm")
                    else:
                        self.textBrowser_ketqua.setText("Phương trình vô nghiệm")

        except ValueError:
            QMessageBox.warning(self, "Lỗi đầu vào", "Vui lòng nhập giá trị hợp lệ cho tất cả hệ số.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ptb3_Window()
    win.show()
    sys.exit(app.exec())
