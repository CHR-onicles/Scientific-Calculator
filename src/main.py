import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from UI_standard_calculator import MainWindow




class MainApp(MainWindow, QMainWindow):

    def __init__(self):
        super(MainApp, self).__init__()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())