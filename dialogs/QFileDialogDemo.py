"""
文件对话框: QFileDialog
"""

import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFileDialogDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文件对话框演示")
        layout = QVBoxLayout()

        self.btn1 = QPushButton("加载图片")
        self.btn1.clicked.connect(self.loadImage)
        layout.addWidget(self.btn1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.btn2 = QPushButton("加载文本文件")
        self.btn2.clicked.connect(self.loadText)
        layout.addWidget(self.btn2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def loadImage(self):
        image, _ = QFileDialog.getOpenFileName(self, "打开文件", ".", "图像文件(*.jpg *.png)")
        self.imageLabel.setPixmap(QPixmap(image))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)     #选择文件
        #dialog.setFileMode(QFileDialog.Directory)  选择文件夹
        dialog.setFilter(QDir.Files)                    #选择文件
        #dialog.setFilter(QDir.Dirs)                选择文件夹
        if dialog.exec():
            fileNames=dialog.selectedFiles()
            f=open(fileNames[0],"r")
            with f:
                data=f.read()
                self.contents.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load("dialogs\Fonts\qt_zh_CN.qm")
    app.installTranslator(translator)

    mainForm = QFileDialogDemo()
    mainForm.show()
    sys.exit(app.exec_())