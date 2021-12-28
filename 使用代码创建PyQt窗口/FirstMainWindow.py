import sys
from PyQt5.QtCore import QFileInfo

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class FirstMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)
#111111111111111
        # 设置主窗口的标题
        self.setWindowTitle("第一个PyQt5主窗口应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage("只存在5秒的消息",5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    root= QFileInfo(__file__).absolutePath()
    app.setWindowIcon(QIcon(root+"/XiuXiu.ico"))
    mainWindow = FirstMainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
