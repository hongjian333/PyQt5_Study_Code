"""
计数器控件（QSpinBox）
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSpinBoxDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("计数器控件演示")
        self.resize(300,100)

        layout=QVBoxLayout()
        self.label=QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.sb=QSpinBox()
        self.sb.setMinimum(0)
        self.sb.setMaximum(1000)
        #self.sb.setRange(0,1000)
        self.sb.setSingleStep(5)
        self.sb.valueChanged.connect(self.valueChange)
        layout.addWidget(self.sb)

        self.setLayout(layout)

    def valueChange(self):
        self.label.setText("当前值 : %s" %str(self.sb.value()))


if __name__ == "__main__":

    app = QApplication(sys.argv)

    form = QSpinBoxDemo()
    form.show()

    sys.exit(app.exec_())