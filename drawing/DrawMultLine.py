"""
绘制不同类型的直线
"""

import sys, math

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


class DrawMultLine(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置Pen的样式")
        self.resize(300, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)

        pen=QPen(Qt.red,3,Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20,120,250,120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20,160,250,160)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        painter.setPen(pen)
        painter.drawLine(20,200,250,200)

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = DrawMultLine()
    mainForm.show()
    sys.exit(app.exec_())
