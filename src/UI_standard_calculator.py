from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import icons_rc



class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Standard Calculator')
        self.setWindowIcon(QIcon(':/icons/calc-icon'))
        self.setFixedSize(500, 700)

        self.widgets()
        self.layouts()

    def widgets(self):
        # <TOP WIDGETS>
        self.calc_screen = QLineEdit()

        # </TOP WIDGETS>

        # <BOTTOM WIDGETS>

        # </BOTTOM WIDGETS>


    def layouts(self):
        pass

