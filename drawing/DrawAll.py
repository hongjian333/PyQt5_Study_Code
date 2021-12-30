"""
绘制各种图形

弧
圆形
椭圆
矩形
多边形
绘制图像

"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPainter, QColor, QFont, QPen, QPolygon
from PyQt5.QtCore import QPoint, QRect, Qt


class DrawAll(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制各种图形")
        self.resize(600, 600)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        #绘制弧，alen: 1个alen等于1/16度
        rect = QRect(0, 10, 100, 100)
        painter.drawArc(rect, 0, 50 * 16)
        #通过弧绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(120, 10, 100, 100, 0, 360 * 16)
        #绘制带弦的弧
        painter.drawChord(10, 120, 100, 100, 12, 130 * 16)
        #绘制扇形
        painter.drawPie(10, 240, 100, 100, 12, 130 * 16)
        #绘制椭圆
        painter.drawEllipse(120, 120, 150, 100)
        #绘制5边形
        point1 = QPoint(140, 380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        polyGon=QPolygon([point1,point2,point3,point4,point5])
        painter.drawPolygon(polyGon)
        #将一个图像绘制到窗口上
        image=QImage("drawing\images\python.jpg")
        rect=QRect(300,400,image.width()/3,image.height()/3)
        painter.drawImage(rect,image)


        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = DrawAll()
    mainForm.show()
    sys.exit(app.exec_())
