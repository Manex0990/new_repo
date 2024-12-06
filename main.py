import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget
from random import randint


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Нажми сюда"))


class Painter(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint_ellipse)

    def paint_ellipse(self):
        qp = QPainter()
        qp.begin(self)
        rad = randint(20, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(color)
        qp.drawEllipse(QPointF(300, 200), rad, rad)
        qp.end()
