# -*- coding: utf-8 -*-
__author__ = 'sergy'

from PyQt4 import QtCore, QtGui
import sp_ch_lib
import sys
import codecs

from spellcheck_ui import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_check.clicked.connect(self.check)

    def check(self):
        check_obj = sp_ch_lib.yandex_spellchecker()
        #text_in = self.ui.textEdit_main.toPlainText()
        text_in = str(unicode(self.ui.textEdit_main.toPlainText()).encode("utf-8"))
        words_t, positions = check_obj.check_text(text_in, str(self.ui.comboBox_lang.currentText()))
        words = []
        for c_word in words_t:
            words.append(str(unicode(c_word).encode('utf-8')))

        new_text = str(unicode(self.ui.textEdit_main.toPlainText()).encode("utf-8"))

        #for position in positions:
        #    pos, len = position
        #    #new_text = new_text[:pos] + unicode('<font color="red">').encode('utf-8') + new_text[pos:pos+len] + unicode('</font>').encode('utf-8') + new_text[pos+len:]
        #    new_text = new_text[:pos+1] + '<font color="red">' + new_text[pos+1:pos+len+2] + '</font>' + new_text[pos+len+2:]

        i = 0
        for word in words:
            pos, c_len = positions[i]
            if (pos == 0) or (pos+c_len-1 == len(text_in)):
                new_text = new_text.replace(word, '<font color="red">' + word + '</font>')
            else:
                new_text = new_text.replace(' ' + word + ' ', '<font color="red"> ' + word + ' </font>')

        self.ui.textEdit_main.clear()
        self.ui.textEdit_main.insertHtml(new_text.decode('utf-8'))

    # http://stackoverflow.com/questions/5506781/pyqt4-application-on-windows-is-crashing-on-exit
    def closeEvent(self, event):
        sys.exit(0)


app = QtGui.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())