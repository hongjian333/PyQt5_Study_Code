"""
字体对话框: QFontDialog
包含如何使用将字体对话框编程中文显示
"""

import sys
from PyQt5 import QtCore

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("字体对话框演示")
        layout=QVBoxLayout()

        self.fontBtn=QPushButton("选择字体")
        self.fontBtn.clicked.connect(self.getFont)
        layout.addWidget(self.fontBtn)

        self.fontLabel=QLabel("hello，测试字体")
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)

    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load("dialogs\Fonts\qt_zh_CN.qm")
    app.installTranslator(translator)

    mainForm = QFontDialogDemo()
    mainForm.show()
    sys.exit(app.exec_())