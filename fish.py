import sys
from PySide6.QtWidgets import QApplication, QWidget , QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap

app = QApplication(sys.argv)
window = QWidget()
pixmap = QPixmap("fish.png")

window.resize(400, 300)

if pixmap.isNull():
    print("no fihh broo")
    sys.exit()


fish = QLabel(window)
fish.setPixmap(pixmap)
fish.resize(pixmap.size())
fish.move(0,0)
window.show()
x = 0
y = 0

def move():
    global x,y
    timer = QTimer()
    timer.timeout.connect(move)
    timer.start(16)
    app.exec()


