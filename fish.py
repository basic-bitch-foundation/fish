import sys
from PySide6.QtWidgets import QApplication, QWidget , QLabel
from PySide6.QtCore import QTimer
app = QApplication(sys.argv)
window = QWidget()
window.show()
window.resize(400, 300)

label = QLabel("hello world", window)


x = 0
y = 0000

window.show
def move():
    global x , y
    x += 2
    y+=2
    window.move(x,y)




move()
timer = QTimer()
timer.timeout.connect(move)
timer.start(16)
    
app.exec()


