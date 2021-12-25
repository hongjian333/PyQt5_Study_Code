import sys

from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow


class CenterForm(QMainWindow):

    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("第一个PyQt5主窗口应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

        # 设置状态蓝信息
        self.status = self.statusBar()
        self.status.showMessage("只存在5秒的消息", 5000)

    def Center(self):
        #获取屏幕尺寸
        screenSize = QDesktopWidget().screenGeometry()
        #获取窗口尺寸
        formSize = self.geometry()
        centerLeft = (screenSize.width()-formSize.width())/2
        centerTop = (screenSize.height()-formSize.height())/2
        #移动窗口
        self.move(centerLeft, centerTop)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    root = QFileInfo(__file__).absolutePath()
    app.setWindowIcon(QIcon(root+"/XiuXiu.ico"))
    mainWindow = CenterForm()
    mainWindow.Center()
    mainWindow.show()

    sys.exit(app.exec_())
