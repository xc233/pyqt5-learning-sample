import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        
        # 获得窗口
        qr = self.frameGeometry()

        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()

        # 将窗口移动到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ec = Example()
    sys.exit(app.exec_())        