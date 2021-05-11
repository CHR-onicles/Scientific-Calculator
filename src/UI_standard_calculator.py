from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import icons_rc, styles



class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Calculator - Standard')
        self.setWindowIcon(QIcon(':/icons/calc-icon'))
        self.setFixedSize(450, 660)
        self.setObjectName('mainwindow')
        self.setStyleSheet(styles.main_window_style())

        self.widgets()
        self.layouts()

    def widgets(self):

        # <TOP WIDGETS>
        self.calc_screen = QLineEdit()
        self.calc_screen.setObjectName('calc-screen')

        # </TOP WIDGETS>


        # <BOTTOM WIDGETS>
        self.all_btns = list()
        for col in range(24):
            new_btn = QPushButton()
            self.all_btns.append(new_btn)
        # </BOTTOM WIDGETS>
        # print(len(self.all_btns), self.all_btns)


    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout = QGridLayout()
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout.setSpacing(3)

        # <TOP LAYOUT>
        self.top_layout.addWidget(self.calc_screen)

        # </TOP LAYOUT>



        # <BOTTOM LAYOUT>
        # lel remove this spaghetti thingy later - brain was tired
        row = 1
        col = 1
        for i in range(24):
            if i % 4 == 0:
                row += 1
                col = 1

            self.bottom_layout.addWidget(self.all_btns[i], row, col)
            if row in [3, 4, 5, 6] and col in [1, 2, 3]:
                self.all_btns[i].setObjectName('num-btn')

            col += 1
        self.all_btns[-1].setObjectName('equal-to-btn')
        # </BOTTOM LAYOUT>

        self.main_layout.addLayout(self.top_layout, 30)

        self.main_layout.addLayout(self.bottom_layout, 70)
        self.setLayout(self.main_layout)

