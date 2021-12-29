import sys

from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow


class IconForm(QMainWindow):

    def __init__(self, parent=None):
        super(IconForm, self).__init__(parent)
        self.initUI()

    # 初始化界面
    def initUI(self):
        # 设置主窗口的标题
        self.setWindowTitle("设置窗口图标")
        # 设置窗口的尺寸
        self.resize(400, 300)
        # 设置窗口图标
        root = QFileInfo(__file__).absolutePath()
        self.setWindowIcon(QIcon(root+"\image\XiuXiu.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = IconForm()
    mainWindow.show()

    sys.exit(app.exec_())
