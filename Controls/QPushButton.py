'''
按钮控件（QPushButton）
'''

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QPushButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButtonDemo")

        formLayout = QVBoxLayout()
        # Toggle Button
        self.button1 = QPushButton("第一个按钮")
        self.button1.setText("First Button")
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        formLayout.addWidget(self.button1)
        # 在按钮文本钱显示图像
        self.button2 = QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap("使用代码创建PyQt窗口\image\python.png")))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))
        formLayout.addWidget(self.button2)
        # 被禁用的按钮
        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)
        formLayout.addWidget(self.button3)
        #有快捷键的按钮
        self.button4=QPushButton("&Download")
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        formLayout.addWidget(self.button4)

        self.setLayout(formLayout)

    def whichButton(self, btn):
        print("被单击的按钮是<"+btn.text()+">")

    def buttonState(self):
        if(self.button1.isChecked()):
            print("按钮1已经被选中")
        else:
            print("按钮1未被选中")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    form = QPushButtonDemo()
    form.show()

    sys.exit(app.exec_())
