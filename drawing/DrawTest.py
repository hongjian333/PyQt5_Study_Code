"""
绘图API: 绘制

1. 文本
2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
3. 图像

必须在paintEvent事件方法中绘制各种元素

"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口上绘制文本")
        self.resize(300, 200)
        self.text = "Python从菜鸟到高手"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont("SimSun", 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = DrawText()
    mainForm.show()
    sys.exit(app.exec_())