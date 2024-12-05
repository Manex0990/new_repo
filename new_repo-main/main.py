import sys
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget
from random import randint


class Painter(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint_ellipse)

    def paint_ellipse(self):
        qp = QPainter()
        qp.begin(self)
        rad = randint(20, 100)
        color = QColor(255, 255, 0)
        qp.setBrush(color)
        qp.drawEllipse(QPointF(300, 200), rad, rad)
        qp.end()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painter()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
