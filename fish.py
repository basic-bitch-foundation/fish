import sys
from PySide6.QtWidgets import QApplication, QWidget , QLabel
app = QApplication(sys.argv)
window = QWidget()
window.show()
label = QLabel("hello world")
label.setParent(window)
label.show()
app.exec()





