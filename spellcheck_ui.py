# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spellcheck_ui.ui'
#
# Created: Sun Mar 22 20:39:36 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_check = QtGui.QPushButton(self.centralwidget)
        self.pushButton_check.setGeometry(QtCore.QRect(10, 565, 98, 27))
        self.pushButton_check.setObjectName(_fromUtf8("pushButton_check"))
        self.comboBox_lang = QtGui.QComboBox(self.centralwidget)
        self.comboBox_lang.setGeometry(QtCore.QRect(120, 565, 71, 27))
        self.comboBox_lang.setObjectName(_fromUtf8("comboBox_lang"))
        self.comboBox_lang.addItem(_fromUtf8(""))
        self.comboBox_lang.addItem(_fromUtf8(""))
        self.comboBox_lang.addItem(_fromUtf8(""))
        self.comboBox_lang.addItem(_fromUtf8(""))
        self.comboBox_lang.addItem(_fromUtf8(""))
        self.textEdit_main = QtGui.QTextBrowser(self.centralwidget)
        self.textEdit_main.setGeometry(QtCore.QRect(10, 40, 781, 521))
        self.textEdit_main.setReadOnly(False)
        self.textEdit_main.setOpenExternalLinks(True)
        self.textEdit_main.setObjectName(_fromUtf8("textEdit_main"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 631, 17))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spellcheck", None))
        self.pushButton_check.setText(_translate("MainWindow", "check", None))
        self.comboBox_lang.setItemText(0, _translate("MainWindow", "ru,en", None))
        self.comboBox_lang.setItemText(1, _translate("MainWindow", "ru", None))
        self.comboBox_lang.setItemText(2, _translate("MainWindow", "en", None))
        self.comboBox_lang.setItemText(3, _translate("MainWindow", "uk", None))
        self.comboBox_lang.setItemText(4, _translate("MainWindow", "en,uk", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>«Проверка правописания: Яндекс.Спеллер» <a href=\"http://api.yandex.ru/speller/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://api.yandex.ru/speller/</span></a></p><p><br/></p><p><br/></p></body></html>", None))

