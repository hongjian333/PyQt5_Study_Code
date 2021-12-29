"""
消息对话框 : QMessageBox

1. 关于对话框
2. 错误对话框
3. 警告对话框
4. 提问对话框
5. 消息对话框
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QMessageBoxDemo(QWidget):

    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("消息对话框演示")
        self.resize(300, 400)

        layout = QVBoxLayout()
        #关于对话框
        self.btn1 = QPushButton("关于对话框", self)
        self.btn1.clicked.connect(self.showDialog)
        layout.addWidget(self.btn1)
        #消息对话框
        self.btn2 = QPushButton("消息对话框", self)
        self.btn2.clicked.connect(self.showDialog)
        layout.addWidget(self.btn2)
        #警告对话框
        self.btn3 = QPushButton("警告对话框", self)
        self.btn3.clicked.connect(self.showDialog)
        layout.addWidget(self.btn3)
        #错误对话框
        self.btn4 = QPushButton("错误对话框", self)
        self.btn4.clicked.connect(self.showDialog)
        layout.addWidget(self.btn4)
        #提问对话框
        self.btn5 = QPushButton("提问对话框", self)
        self.btn5.clicked.connect(self.showDialog)
        layout.addWidget(self.btn5)

        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()

        if text == "关于对话框":
            QMessageBox.about(self, "关于", "这是一个关于对话框")
        elif text == "消息对话框":
            reply = QMessageBox.information(self, "消息", "这是一个消息对话框", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply==QMessageBox.Yes)
        elif text=="警告对话框":
            reply = QMessageBox.warning(self, "警告", "这是一个警告对话框", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text=="错误对话框":
            reply = QMessageBox.critical(self, "错误", "这是一个错误对话框", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif text=="提问对话框":
            reply = QMessageBox.question(self, "提问", "这是一个提问对话框", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = QMessageBoxDemo()
    mainForm.show()
    sys.exit(app.exec_())