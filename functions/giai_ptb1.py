from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from py_ui.ptb1Widget import Ui_ptb1_window  
import sys

class Ptb1_Window(QMainWindow, Ui_ptb1_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Giải Phương trình bậc 1")
        
        # Connect the button to the solve function
        self.button_giai.clicked.connect(self.Giai_ptb1)
    
    @Slot()
    def Giai_ptb1(self):
        try:
            # Read coefficients from input fields
            a = float(self.textBrowser_hs1.text())
            b = float(self.textBrowser_hs2.text())
            
            # Solve the equation ax + b = 0
            if a == 0:
                if b == 0:
                    result = "Phương trình có vô số nghiệm."  # The equation has infinitely many solutions
                else:
                    result = "Phương trình vô nghiệm."  # The equation has no solution
            else:
                x = -b / a
                result = f"{x:.2f}"
            
            # Display the result
            self.textBrowser_ketqua.setText(result)
        
        except ValueError:
            # Show error message if input is not valid
            QMessageBox.warning(self, "Invalid Input", "Vui lòng nhập hệ số hợp lệ.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ptb1_Window()
    window.show()
    sys.exit(app.exec())
