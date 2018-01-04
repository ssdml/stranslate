#!/usr/bin/env python

from translate.yatranslate import YaTranslate
from windows.mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Program:
    def __init__(self):
        key = self.load_key()
        translator = YaTranslate(key)

        app = QApplication(sys.argv)

        main = MainWindow(translator)

        if len(sys.argv) > 1 and sys.argv[1]:
            main.setInputText(sys.argv[1])

        main.show()

        sys.exit(app.exec_())

    def load_key(self):
        with open('key.txt', 'r') as key_file:
            key = key_file.read()
        key = key.strip()
        return key

if __name__ == '__main__':
    Program()