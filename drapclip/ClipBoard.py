"""
使用剪贴板

"""

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *


class ClipBoardDemo(QDialog):

    def __init__(self):
        super().__init__()
        textCopyBtn = QPushButton("复制文本")
        textPasteBtn = QPushButton("粘贴文本")

        htmlCopyBtn = QPushButton("复制HTML")
        htmlPasteBtn = QPushButton("粘贴HTML")

        imageCopyBtn = QPushButton("复制图像")
        imagePasetBtn = QPushButton("粘贴图像")

        self.textLabel = QLabel("默认文本")
        self.imageLabel = QLabel()
        #self.imageLabel.setPixmap(QtGui.QPixmap("drapclip\images\python.jpg"))

        layout = QGridLayout()
        layout.addWidget(textCopyBtn, 0, 0)
        layout.addWidget(imageCopyBtn, 0, 1)
        layout.addWidget(htmlCopyBtn, 0, 2)
        layout.addWidget(textPasteBtn, 1, 0)
        layout.addWidget(imagePasetBtn, 1, 1)
        layout.addWidget(htmlPasteBtn, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        self.setLayout(layout)

        textCopyBtn.clicked.connect(self.copyText)
        textPasteBtn.clicked.connect(self.pasteText)
        imageCopyBtn.clicked.connect(self.copyImage)
        imagePasetBtn.clicked.connect(self.pasteImage)
        htmlCopyBtn.clicked.connect(self.copyHtml)
        htmlPasteBtn.clicked.connect(self.pasteHtml)

        self.setWindowTitle("剪贴板演示")

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("hello world")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QtGui.QPixmap("drapclip\images\python.jpg"))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData=clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = ClipBoardDemo()
    mainForm.show()
    sys.exit(app.exec_())