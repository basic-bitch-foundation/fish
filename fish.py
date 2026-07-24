import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QTransform

app = QApplication(sys.argv)

pixmap = QPixmap("fish.png")

if pixmap.isNull():
    print("Couldn't load fish.png")
    sys.exit()


right_pixmap = pixmap
left_pixmap = pixmap.transformed(QTransform().scale(-1, 1))

window = QWidget()
window.setWindowTitle("Fish")
window.resize(pixmap.width(), pixmap.height())

fish = QLabel(window)
fish.setPixmap(right_pixmap)
fish.resize(pixmap.size())
fish.move(0, 0)

window.show()

screen = app.primaryScreen().availableGeometry()

x = 100
y = 100

vx = 5
vy = 3

window.move(x, y)


def move():
    global x, y, vx, vy

    x += vx
    y += vy

    if x <= screen.left():
        x = screen.left()
        vx = abs(vx)

    elif x + window.width() >= screen.right():
        x = screen.right() - window.width()
        vx = -abs(vx)

    if y <= screen.top():
        y = screen.top()
        vy = abs(vy)

    elif y + window.height() >= screen.bottom():
        y = screen.bottom() - window.height()
        vy = -abs(vy)

    
    if vx > 0:
        fish.setPixmap(right_pixmap)
    else:
        fish.setPixmap(left_pixmap)

    window.move(x, y)


timer = QTimer()
timer.timeout.connect(move)
timer.start(16)  

sys.exit(app.exec())
