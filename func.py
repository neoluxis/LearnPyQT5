import os

from PyQt5 import QtCore, QtGui, QtWidgets

from config import *


def refresh_themes(window):
    themes = os.listdir(theme_folder)
    # print(themes)
    for i in range(len(themes)):
        item = window.lstThemes.item(i)
        item.setText(themes[i])
        


if __name__ == "__main__":
    refresh_themes()
