from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Map Editor")
        self.init_UI()

    def init_UI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(150, 150)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Button 1")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("pressed")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())


window()
