"""
让空间支持拖拽动作
A
B.setAcceptDrops(True)

B需要两个事件
1. dragEnterEvent           将A拖到B触发
2. dropEvent                    在B的区域放下   A时触发
"""

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class MyComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        self.addItem(e.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        formLayout=QFormLayout()
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)       #让控件可拖动

        cb=MyComboBox()
        formLayout.addRow(lineEdit,cb)
        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = DrapDropDemo()
    mainForm.show()
    sys.exit(app.exec_())

