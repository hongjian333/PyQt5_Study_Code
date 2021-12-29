import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QWidget


class QuitAppForm(QMainWindow):

    def __init__(self):
        super(QuitAppForm, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle("如何退出应用程序")
        # 设置窗口的尺寸
        self.resize(400, 300)
        # 添加一个Button
        self.btn = QPushButton("退出应用程序")
        self.btn.clicked.connect(self.onClick_Button)
        # 把按钮添加到窗体上
        layout = QHBoxLayout()
        layout.addWidget(self.btn)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    # 点击按钮事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+"按钮被按下")
        app = QApplication.instance()
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = QuitAppForm()
    mainForm.show()
    sys.exit(app.exec_())
