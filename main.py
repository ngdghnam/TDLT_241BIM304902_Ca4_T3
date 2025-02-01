import sys
from PySide6.QtWidgets import QApplication
from process import Widget

app = QApplication(sys.argv)
# app = QApplication([])

window = Widget()
window.show()

app.exec()