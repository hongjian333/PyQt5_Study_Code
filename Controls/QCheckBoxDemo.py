'''
复选框控件:

3中状态

未选中 : 0
半选中 : 1
选中 : 2
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框控件演示")

        formLayout=QHBoxLayout()

        self.checkBox1=QCheckBox("复选框控件1")
        self.checkBox1.setChecked(True)
        self.checkBox1.toggled.connect(self.checkBoxState)
        formLayout.addWidget(self.checkBox1)

        self.checkBox2=QCheckBox("复选框控件2")
        self.checkBox2.toggled.connect(self.checkBoxState)
        formLayout.addWidget(self.checkBox2)

        self.checkBox3=QCheckBox("复选框控件3")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(self.checkBoxState)
        formLayout.addWidget(self.checkBox3)        

        self.setLayout(formLayout)


    def checkBoxState(self):
        chk1Status = self.checkBox1.text()+", isChecked="+  str( self.checkBox1.isChecked() ) + ', chekState=' + str(self.checkBox1.checkState())   +"\n"
        chk2Status = self.checkBox2.text()+", isChecked="+  str( self.checkBox2.isChecked() ) + ', checkState=' + str(self.checkBox2.checkState())   +"\n"
        chk3Status = self.checkBox3.text()+", isChecked="+  str( self.checkBox3.isChecked() ) + ', checkState=' + str(self.checkBox3.checkState())   +"\n"
        print(chk1Status + chk2Status + chk3Status )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QCheckBoxDemo()
    mainWindow.show()

    sys.exit(app.exec_())
