"""
下拉列表控件（QComboBox）

1. 如何将列表项添加到控件中
2. 如何获取选中列表项
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(200, 100)

        layout = QVBoxLayout()

        self.label = QLabel("请选择编程语言")

        self.cb = QComboBox()
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java", "C#", "Ruby"])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        layout.addWidget(self.label)
        self.setLayout(layout)
 
    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            #print("item" + str(count) + "=" + self.cb.itemText(count))
            print("item%s = %s" %(str(count),self.cb.itemText(count)))
            #print("current index", i, "selection changed", self.cb.currentText())
            print("current index %s selection changed %s" %(i,self.cb.currentText()))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QComboBoxDemo()
    mainWindow.show()

    sys.exit(app.exec_())