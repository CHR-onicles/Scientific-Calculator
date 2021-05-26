import sys
import textwrap

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from UI_standard_calculator import UiMainWindow




class MainApp(UiMainWindow, QMainWindow):

    def __init__(self):
        super(MainApp, self).__init__()

        self.widgets()

    def widgets(self):
        # <NUMBER BUTTONS>
        # print(self.all_btns.index('0'))
        for x in self.all_btns:
            x.clicked.connect(lambda: self.on_num_btn_click(x))
            print(x.text())
            # break

        # </NUMBER BUTTONS>
        pass

    def on_num_btn_click(self, btn):
        # is_btn_found = False
        print(btn.text())

        if btn.text() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.calc_screen.setText(self.calc_screen.text() + btn.text())
            # is_btn_found = True
            # break





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
