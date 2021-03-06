'''
QLineEdit控件与回显模式

基本功能 : 输入单行文本

EchoMode（回显模式）:

4种回显模式

1. Normal
2. NoEcho : 不显示在屏幕上
3. Password
4. PasswordEchoEdit : 前1~2秒正常显示，后面变成 *
'''
import sys

from PyQt5.QtWidgets import *


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框回显模式")

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoLineEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("noEchoLineEdit", noEchoLineEdit)
        formLayout.addRow("passwordLineEdit", passwordLineEdit)
        formLayout.addRow("passwordEchoLineEdit", passwordEchoLineEdit)

        # placeholdertext 输入前显示的文字
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("noEcho")
        passwordLineEdit.setPlaceholderText("password")
        passwordEchoLineEdit.setPlaceholderText("passwordEcho")

        #设置EchoMode
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = QLineEditEchoMode()
    mainForm.show()

    sys.exit(app.exec_())
