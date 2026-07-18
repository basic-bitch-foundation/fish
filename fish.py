import sys
from PySide6.QtWidgets import QApplication, QWidget , QLabel
from PySide6.QtCore import QTimer
app = QApplication(sys.argv)
window = QWidget()
window.show()
window.resize(400, 300)

label = QLabel("hello world", window)



label.show()
x =0
y = 0


def move():
    global x, y
    x += 1
    y += 1
    label.move(x,y)

move()
timer = QTimer()
timer.timeout.connect(move)
timer.start(30)
    
app.exec()







