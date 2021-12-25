'''
QLineEdit控件的输入（校验器）

例如限制只能输入数字、整数、浮点数或满足一定条件的字符串
'''

import sys

from PyQt5.QtCore import QLocale, QRegExp
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import *


class QlineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("输入数据校验器")

        # 创建LIneEdit
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        # 创建表单布局
        formLayout = QFormLayout()
        formLayout.addRow("整数类型", intLineEdit)
        formLayout.addRow("浮点类型", doubleLineEdit)
        formLayout.addRow("数字和字母", validatorLineEdit)

        # 设置输入前提示文本
        intLineEdit.setPlaceholderText("整数")
        doubleLineEdit.setPlaceholderText("浮点数")
        validatorLineEdit.setPlaceholderText("字母和数字")

        # 整数校验器1~99
        intValidator = QIntValidator()
        intValidator.setRange(1, 99)
        intLineEdit.setValidator(intValidator)

        # 浮点校验器-360~360,精度：小数点后2位
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)  # 设置精度：小数点后2位
        doubleLineEdit.setValidator(doubleValidator)

        # 字符和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        validator = QRegExpValidator()
        validator.setRegExp(reg)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainForm = QlineEditValidator()
    mainForm.show()

    sys.exit(app.exec_())
