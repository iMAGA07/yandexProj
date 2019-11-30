import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QRadioButton, QVBoxLayout, QStatusBar
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog, QPlainTextEdit
from PyQt5.QtGui import QPixmap
from ui_filebir import Ui_MainWindow
from win10toast import ToastNotifier
import time
import sqlite3
import easygui 
from tkinter import filedialog
from tkinter import *


class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(520, 300)

        self.pushButton.clicked.connect(self.notepad_run)
        self.re_but.clicked.connect(self.reminder_run)
        self.pushButton_2.clicked.connect(self.dbrun)
        self.rate = self.lineEdit.text()
        

    def dbrun(self):
        pass
        #con = sql.connect('dbrate.db')
        #cur = con.cursor()
        #cur.execute(query)
        #res = cur.execute(query)
        #con.commit()
        #con.close()


    def notepad_run(self):
        self.uineweki = fileeki()
        self.uineweki.show()
        self.close()
    
    def reminder_run(self):
        self.ui_fileush = fileush()
        self.ui_fileush.show()
        self.close()


class fileeki(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        uic.loadUi('uineweki.ui', self)

        self.editor = QPlainTextEdit()

        self.path = None

        self.pushButton.clicked.connect(self.opening_run)
        self.pushButton_2.clicked.connect(self.saving_run)
        self.pushButton_3.clicked.connect(self.saveac)
        self.pushButton_4.clicked.connect(self.bak)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def opening_run(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)

    def saving_run(self):
        if self.path is None:

            return self.saveac()

        self._save_to_path(self.path)

    def saveac(self):
        path = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            
            return
        
        self._save_to_path(self.path)
            
    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def new_run(self):
        pass

    def bak(self):
        self.close()
        self.nazad = MyWidget()
        self.nazad.show()
    

class fileush(QWidget):
    def __init__(self, *args):
        super().__init__()

        uic.loadUi('ui_fileush.ui', self)
        self.pushButton.clicked.connect(self.running)
        self.pushButton_2.clicked.connect(self.bakk)

    def running(self):
        toaster = ToastNotifier()

        self.first_input = self.lineEdit.text()
        self.second_input = self.lineEdit_2.text()

        t = time.sleep(int(self.first_input))
        toaster.show_toast(self.second_input)
    

    def bakk(self):
        self.close()
        self.nazad = MyWidget()
        self.nazad.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
