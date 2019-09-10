import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Examle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('zetcode', self)
        lbl1.move(30, 30)

        lbl2 = QLabel('coder', self)
        lbl2.move(50, 50)

        lbl3 = QLabel('programmer', self)
        lbl3.move(80, 80)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ec = Examle()
    sys.exit(app.exec_())