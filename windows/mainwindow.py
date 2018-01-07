#!/usr/bin/python3
# -*- coding: utf-8 -*-

from windows.ui_mainwindow import Ui_MainWindow
from translate.yatranslate import YaTranslate
from functools import lru_cache
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, translator: YaTranslate):
        super().__init__()
        self._translator = translator

        self.setupUi(self)
        self.moveToCenter()

        self.translate_button.clicked.connect(self.translate)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.translate()
        else:
            super().keyPressEvent(event)

    def setInputText(self, text=""):
        self.input_text.setText(text)

    def translate(self):
        text = self.input_text.toPlainText().strip()
        language = "ru"
        if text:
            if (self.language_select.currentIndex() == 1):
                language = "en"
            self.translated_text.setText(self._translator.translate(text, language))

    def moveToCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())