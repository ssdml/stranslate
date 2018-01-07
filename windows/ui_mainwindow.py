# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 371)
        MainWindow.setStyleSheet("text-align: center;")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.translate_button = QtWidgets.QPushButton(self.centralWidget)
        self.translate_button.setGeometry(QtCore.QRect(200, 300, 111, 31))
        self.translate_button.setObjectName("translate_button")
        self.input_text = QtWidgets.QTextEdit(self.centralWidget)
        self.input_text.setGeometry(QtCore.QRect(20, 20, 491, 111))
        self.input_text.setObjectName("input_text")
        self.translated_text = QtWidgets.QTextBrowser(self.centralWidget)
        self.translated_text.setGeometry(QtCore.QRect(20, 150, 491, 111))
        self.translated_text.setObjectName("translated_text")
        self.language_select = QtWidgets.QComboBox(self.centralWidget)
        self.language_select.setGeometry(QtCore.QRect(20, 300, 131, 31))
        self.language_select.setObjectName("language_select")
        self.language_select.addItem("")
        self.language_select.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перевод"))
        self.translate_button.setText(_translate("MainWindow", "Перевести"))
        self.translated_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.language_select.setItemText(0, _translate("MainWindow", "на русский", "RU"))
        self.language_select.setItemText(1, _translate("MainWindow", "на английский", "EN"))

