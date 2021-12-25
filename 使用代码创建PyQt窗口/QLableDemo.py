import sys

from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置主窗口的标题
        self.setWindowTitle("QLabel使用")
        # 设置窗口的尺寸
        self.resize(500, 500)
        # 设置QLabel
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        # lable1设置
        label1.setText("<font color = yellow>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)                      #设置自动填充背景
        palette = QPalette()                                               #创建调色板
        palette.setColor(QPalette.Window, Qt.blue)         #设置label1背景颜色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        # lable2设置
        label2.setText("<a href = '#'>欢迎使用Python GUI程序</a>")
        label2.linkHovered.connect(self.linkHovered)          #设置信号与槽
        # label3设置
        label3.setToolTip("这是一个图片")
        label3.setAlignment(Qt.AlignCenter)
        label3.setPixmap(QPixmap("使用代码创建PyQt窗口\image\pic.PNG"))
        # label4设置
        label4.setText("<a href = https://www.baidu.com>百度搜索</a>")
        label4.setOpenExternalLinks(True)                          #设置可以打开网页链接（True）
                                                                                        #绑定槽函数（False）
        label4.linkActivated.connect(self.linkClicked)         #设置信号与槽
        #设置布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        self.setLayout(vbox)

    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")

    def linkClicked(self):
        print("当属表单击label4标签时，触发事件")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QLabelDemo()
    mainWindow.show()

    sys.exit(app.exec_())
