from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.tong_day import Ui_Summation_Widget

class Find_Summation(QMainWindow, Ui_Summation_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Summation")

        self.button_giai.clicked.connect(self.tongDaySo)

    @Slot()
    def tongDaySo(self):
        try:
            start = float(self.input_start.text())
            end = float(self.input_end.text())
            result = self.tinh_tong_day_so(start, end)
            self.textBrowser_ketqua.setText(f"Summation({start}, {end}): {result}")
        except ValueError:
            self.textBrowser_ketqua.setText("Error: Invalid")

    @staticmethod
    def tinh_tong_day_so(start, end):
    # Đảm bảo rằng a nhỏ hơn hoặc bằng b
        if start > end:
            return ("Giá trị bắt đầu phải nhỏ hơn hoặc bằng giá trị kết thúc.")
        
        # Sử dụng công thức tính tổng dãy số từ a đến b
        n = end - start + 1  # Số lượng phần tử trong dãy
        Tong = (n * (start + end)) // 2  # Tính tổng theo công thức (n * (a + b)) / 2

        return Tong