'''
单选按钮控件（QRadioButton）
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton")

        formLayout = QHBoxLayout()

        self.button1 = QRadioButton("单选按钮1")
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState)
        formLayout.addWidget(self.button1)

        self.button2=QRadioButton("单选按钮2")
        self.button2.toggled.connect(self.buttonState)
        formLayout.addWidget(self.button2)

        self.setLayout(formLayout)

    def buttonState(self):
        sender = self.sender()
        if(sender.text() == "单选按钮1"):
            if(sender.isChecked()):
                print("<"+sender.text()+">被选中")
            else:
                print("<"+sender.text()+">未被选中")
        if(sender.text() == "单选按钮2"):
            if(sender.isChecked()):
                print("<"+sender.text()+">被选中")
            else:
                print("<"+sender.text()+">未被选中")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    form = QRadioButtonDemo()
    form.show()

    sys.exit(app.exec_())

