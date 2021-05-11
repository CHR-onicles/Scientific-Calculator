from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Standard Calculator')
        self.setFixedSize(500, 700)

        self.widgets()
        self.layouts()

    def widgets(self):
        pass

    def layouts(self):
        pass

