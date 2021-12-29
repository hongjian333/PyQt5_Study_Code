"""
输入对话框: QInputDialog

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getint
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QInputDialogDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("输入对话框演示")
        layout = QFormLayout()

        self.btn1 = QPushButton("获取列表中的选项")
        self.btn1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.btn1, self.lineEdit1)

        self.btn2 = QPushButton("获取字符串")
        self.btn2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.btn2, self.lineEdit2)

        self.btn3 = QPushButton("获取整数")
        self.btn3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.btn3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ["C", "C++", "Ruby", "Python", "Java", "C#"]
        item, ok = QInputDialog.getItem(self, "请选择编程预算", "语言列表", items)
        if ok and item :
            self.lineEdit1.setText(item)
    
    def getText(self):
        text, ok = QInputDialog.getText(self, "文本输入框", "输入姓名")
        if ok and text  :
            self.lineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "数字输入框", "输入年龄")
        if ok and num :
            self.lineEdit3.setText(str(num))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = QInputDialogDemo()
    mainForm.show()
    sys.exit(app.exec_())