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

        self.all_btns_text = ('%', 'CE', 'C', '',
                              '1/x', '', '', '',
                              '7', '8', '9', '',
                              '4', '5', '6', '',
                              '1', '2', '3', '',
                              '+/_', '0', '.', '',
                              )

        self.widgets()
        self.layouts()

    def widgets(self):

        # <TOP WIDGETS>
        self.calc_screen = QLineEdit()
        self.calc_screen.setObjectName('calc-screen')
        self.calc_screen.setAlignment(Qt.AlignRight)

        # </TOP WIDGETS>


        # <BOTTOM WIDGETS>
        self.all_btns = list()
        for i in range(24):
            new_btn = QPushButton()
            self.all_btns.append(new_btn)

        self.all_btns[-1].setObjectName('equal-to-btn')
        self.all_btns[-1].setIcon(QIcon(':/icons/equal-to'))
        self.all_btns[3].setIcon(QIcon(':/icons/backspace'))
        self.all_btns[11].setIcon(QIcon(':/icons/multiplication'))
        self.all_btns[15].setIcon(QIcon(':/icons/subtraction'))
        self.all_btns[7].setIcon(QIcon(':/icons/division'))
        self.all_btns[19].setIcon(QIcon(':/icons/addition'))
        self.all_btns[6].setIcon(QIcon(':/icons/square-root'))
        self.all_btns[5].setIcon(QIcon(':/icons/squared2'))

        self.all_btns[5].setIconSize(QSize(25, 25))
        self.all_btns[6].setIconSize(QSize(23, 23))
        self.all_btns[19].setIconSize(QSize(23, 23))
        self.all_btns[7].setIconSize(QSize(20, 20))
        self.all_btns[11].setIconSize(QSize(15, 15))
        self.all_btns[15].setIconSize(QSize(20, 20))
        self.all_btns[3].setIconSize(QSize(23, 23))
        self.all_btns[-1].setIconSize(QSize(20, 23))

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
        # remove this spaghetti thingy later - brain was tired
        row = 1
        col = 1
        for i in range(24):
            if i % 4 == 0:
                row += 1
                col = 1

            self.bottom_layout.addWidget(self.all_btns[i], row, col)
            if row in [4,5,6,7] and col in [1, 2, 3]:  # fixme: rows supposed to be 3,4,5,6 but idk something wrong...
                self.all_btns[i].setObjectName('num-btn')

            self.all_btns[i].setText(self.all_btns_text[i])
            # print(self.all_btns[i], self.all_btns_text[i])

            col += 1


        # </BOTTOM LAYOUT>

        self.main_layout.addLayout(self.top_layout, 30)
        self.main_layout.addLayout(self.bottom_layout, 70)
        self.setLayout(self.main_layout)

