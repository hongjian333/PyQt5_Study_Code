'''
QTextEdit控件
'''

import sys

from PyQt5.QtWidgets import *


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")
        self.resize(300, 200)

        formLayout = QVBoxLayout()

        self.textEdit = QTextEdit()
        self.btnText = QPushButton("显示文本")
        self.btnHtml = QPushButton("显示Html")
        self.btnToText = QPushButton("获取文本")
        self.btnToHtml = QPushButton("获取Html")

        self.btnText.clicked.connect(self.onClickedBtnText)
        self.btnHtml.clicked.connect(self.onClickedBtnHtml)
        self.btnToText.clicked.connect(self.onClickedBtnToText)
        self.btnToHtml.clicked.connect(self.onClickedBtnToHtml)

        formLayout.addWidget(self.textEdit)
        formLayout.addWidget(self.btnText)
        formLayout.addWidget(self.btnHtml)
        formLayout.addWidget(self.btnToText)
        formLayout.addWidget(self.btnToHtml)

        self.setLayout(formLayout)

    def onClickedBtnText(self):
        self.textEdit.setPlainText("Holle world")

    def onClickedBtnHtml(self):
        self.textEdit.setHtml(
            "<font color='blue' size='500'>Hello World</font>")

    def onClickedBtnToText(self):
        print(self.textEdit.toPlainText())

    def onClickedBtnToHtml(self):
        print(self.textEdit.toHtml())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = QTextEditDemo()
    form.show()

    sys.exit(app.exec_())
