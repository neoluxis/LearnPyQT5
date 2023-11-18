import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from nui import Ui_MainWindow
from config import *
from func import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
