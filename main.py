import sys
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = -1
        self.y = -1
        self.radius = 0
        self.f = False
        self.qp = QPainter()
        self.btn.clicked.connect(self.trigger)

    def trigger(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.radius = randint(1, 100)
        self.x = randrange(50, 800)
        self.y = randrange(50, 600)
        color = QColor(randrange(0, 255, 1), randrange(0, 255, 1), randrange(0, 255, 1))
        self.qp.setBrush(color)
        self.qp.drawEllipse(self.x, self.y, self.radius, self.radius)

    def initUI(self):
        self.setGeometry(0, 0, 950, 650)
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(450, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())