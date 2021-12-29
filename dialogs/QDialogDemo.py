"""
对话框QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

QMainWindow
QWidget
QDialog
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDialogDemo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("对话框演示")
        self.resize(300,200)

        self.btn=QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50,50)
        self.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        dialog=QDialog()
        dialog.setWindowTitle("对话框")
        dialog.setWindowModality(Qt.ApplicationModal)
        btn=QPushButton("确定",dialog)
        btn.clicked.connect(dialog.close)
        btn.move(50,50)

        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = QDialogDemo()
    mainForm.show()
    sys.exit(app.exec_())