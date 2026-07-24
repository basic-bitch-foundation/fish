import sys
from PySide6.QtWidgets import QApplication, QWidget , QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QTransform

app = QApplication(sys.argv)
window = QWidget()
pixmap = QPixmap("fish.png")

window.resize(1960, 1080)

if pixmap.isNull():
    print("no fihh broo")
    sys.exit()
right_pixmap = pixmap
left_pixmap = pixmap.transformed(QTransform().scale(-1,1))


fish = QLabel(window)
fish.setPixmap(pixmap)
fish.resize(pixmap.size())
fish.move(0,0)

x = 0
y = 0
vx = 5
vy = 3

fish.move(x,y)
window.show()
def move():
    global x,y,vx,vy
    x += vx
    y += vy
    if x <= 0:
        x =0
        vx= abs(vx)
    elif x  + fish.width() >= window.width():
        x = window.width() - fish.width()
        vx = -abs(vx)

    if y <= 0:
        y =0
        vy = abs(vy)
    elif y + fish.height() >= window.height():
        y= window.height() -fish.height()
        vy = -abs(vy)
    if vx>0:
        fish.setPixmap(right_pixmap)
    else:
        fish.setPixmap(left_pixmap)
    
    fish.move(x,y)

move()

timer = QTimer()
timer.timeout.connect(move)
timer.start(16)



sys.exit(app.exec())



