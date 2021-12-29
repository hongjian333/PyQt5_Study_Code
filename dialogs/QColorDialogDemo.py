"""
颜色对话框
"""

import sys
from PyQt5 import QtCore

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QColorDialogDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("颜色对话框演示")
        self.resize(300, 200)
        layout = QVBoxLayout()

        self.colorBtn = QPushButton("选择颜色")
        self.colorBtn.clicked.connect(self.getColor)
        layout.addWidget(self.colorBtn)

        self.colorBtn1 = QPushButton("选择背景颜色")
        self.colorBtn1.clicked.connect(self.getBgColor)
        layout.addWidget(self.colorBtn1)

        self.colorLabel = QLabel("hello，测试颜色")
        self.colorLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)
    
    def getBgColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load("dialogs\Fonts\qt_zh_CN.qm")
    app.installTranslator(translator)

    mainForm = QColorDialogDemo()
    mainForm.show()
    sys.exit(app.exec_())