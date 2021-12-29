"""
滑块控件（QSlider）
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSliderDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("滑块控件演示")
        self.resize(300,100)

        layout=QVBoxLayout()

        self.label=QLabel("你好 PyQt5")
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider=QSlider(Qt.Horizontal)
        #self.slider=QSlider(Qt.Vertical)
        self.slider.setMinimum(12)              #设置最小值
        self.slider.setMaximum(48)              #设置最大值
        self.slider.setSingleStep(3)                #设置步长
        self.slider.setValue(18)                    #设置当前值
        self.slider.setTickPosition(QSlider.TicksBelow)             #设置刻度的位置
        self.slider.setTickInterval(6)      #设置刻度的间隔
        self.slider.valueChanged.connect(self.valueChagne)

        layout.addWidget(self.slider)
        self.setLayout(layout)

    def valueChagne(self):
        print("当前值 : %s" %self.slider.value())
        size=self.slider.value()
        self.label.setFont(QFont("Arial",size))
        
if __name__ == "__main__":

    app = QApplication(sys.argv)

    form = QSliderDemo()
    form.show()

    sys.exit(app.exec_())

