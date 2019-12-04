import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QTimeEdit
from plyer import notification
import time
import sqlite3 as sql
from datetime import datetime
from ui_filebir import Ui_MainWindow

# импортирование нужных модулей для запуска программы

didgi = []
gigid = []

for we in range(1, 11):
    didgi.append(str(we))
 
for me in range(1, 7):
    gigid.append(str(me))

# Создание списка и цикла для ввода оценки от 0 до 11


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('ph.ico'))
        self.rer = didgi
        self.mam = gigid
        self.setupUi(self)
        self.resize(520, 300)

# Создание класса и основной функийй
# Начальный свойчтва глоавного окна

        self.pushButton.clicked.connect(self.notepad_run)
        self.re_but.clicked.connect(self.reminder_run)
        self.pushButton_2.clicked.connect(self.dbrun)

# Связывание обьектов с функциями

    def dbrun(self):
        qe = self.lineEdit.text()
        if str(qe) not in self.rer:

            notification.notify(
                title='WARNING)',
                message='Pls write number from 1 to 10',
                app_icon='ph.ico',
                timeout=6,)

        elif str(qe) in self.mam:
            self.recom_run()

        elif str(qe) in self.rer:
            con = sql.connect('dbrate.db')
            cur = con.cursor()
            query = '''INSERT INTO WW (desh) VALUES (?)'''
            res = cur.execute(query, (qe,))
            con.commit()
            con.close()

            notification.notify(
            title='NOTIFICATION)',
            message='Your mark was submitted',
            app_icon='ph.ico',
            timeout=6,)

# Функция для записи оценок в базу данных

    def recom_run(self):
        self.uifiletort = filerecom()
        self.uifiletort.show()
        self.close()

# Функция для связки первого окна

    def notepad_run(self):
        self.uineweki = fileeki()
        self.uineweki.show()
        self.close()

# Функция для связки второго окна

    def reminder_run(self):
        self.ui_fileush = fileush()
        self.ui_fileush.show()
        self.close()

# Функция для связки третьего окна
# функция создана для записи оценки
# Пользователь должен ввести оценку от 1 до 10
# В противном случае программа выведет ошибку

class filerecom(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('ph.ico'))
        uic.loadUi('uifiletort.ui', self)
        self.resize(520, 400)

        self.pushButton.clicked.connect(self.submitting)
        self.pushButton_2.clicked.connect(self.bakk)


# Создание нового класса для окна рекомендации
# Добавление основной функции
# Загрузка интерфейса в формате ui
        

    def submitting(self):
        text = self.plainTextEdit.toPlainText()
        con = sql.connect('dbrate.db')
        cur = con.cursor()
        query = '''INSERT INTO QQ (DE) VALUES (?)'''
        res = cur.execute(query, (text,))
        con.commit()
        con.close()

        notification.notify(
            title='NOTIFICATION)',
            message='Your recommendation was submitted',
            app_icon='ph.ico',
            timeout=6,)

# Функция для записи рекомендации в базу данных

    def bakk(self):
        self.close()
        self.nazad = MyWidget()
        self.nazad.show()

# Функция для возвращения на главную страницу

class fileeki(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('ph.ico'))
        uic.loadUi('uineweki.ui', self)

# Создание нового класса для блокнота
# Добавление основной функции
# Загрузка интерфейса в формате ui

        self.put = None

# put хранит путь к открытому файлу

        self.pushButton.clicked.connect(self.opening)
        self.pushButton_2.clicked.connect(self.saving_run)
        self.pushButton_3.clicked.connect(self.saveac)
        self.pushButton_4.clicked.connect(self.bak)

# Связывание обьектов с функциями

    def ketpe(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def opening(self):
        put, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")

        if put:
            try:
                with open(put, 'rU') as reading:
                    text = reading.read()

            except Exception as e:
                self.ketpe(str(e))

            else:
                self.put = put
                self.plainTextEdit.setPlainText(text)

# Функция для открытия файла в формате txt
# Для открытия используется обьект QFileDialog, он открывает проводник

    def saving_run(self):
        if self.put is None:

            return self.saveac()

        self.sp(self.put)

# Функция для сохранения файла в формате txt
# Если был открыт не сущесвующий файл, то выполняется следущая функция

    def saveac(self):
        put, filter = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")

        if not put:
            return
        self.sp(put)

# Функция для сохранения нового файла в формате txt по введенному путю

    def sp(self, put):
        text = self.plainTextEdit.toPlainText()
        try:
            with open(put, 'w') as reading:
                reading.write(text)

        except Exception as alma:
            self.ketpe(str(alma))

        else:
            self.put = put
            notification.notify(
                title='Notification from iMAGA)',
                message='Your note was saved',
                app_icon='ph.ico',
                timeout=6,)

# Функция для сохранения файла в формате txt спомощью пути

    def bak(self):
        self.close()
        self.nazad = MyWidget()
        self.nazad.show()

# Функция для возвращения на главную страницу


class fileush(QWidget):
    def __init__(self, *args):
        super().__init__()

# Создание нового класса для Reminder
# Создвние основной функции

        uic.loadUi('ui_fileush.ui', self)
        self.setWindowIcon(QtGui.QIcon('ph.ico'))
        self.pushButton.clicked.connect(self.running)
        self.pushButton_2.clicked.connect(self.bakk)

# Загрузка интерфейса в формате ui
# Связывание обьектов с функциями

    def running(self):
        self.now = datetime.now()
        self.tmf = self.tm.time()

# Считывание времени указанной в программе и в реальности

        self.uak = self.tmf.toString()
        self.current_time = self.now.strftime("%H:%M:%S")
        self.seku = self.current_time.split(":")
        self.seku2 = self.uak.split(":")
        self.seknot = 3600 * (int(self.seku2[0])) + (int(self.seku2[1])) * 60
        self.sekcur = 3600 * (int(self.seku[0])) + (int(self.seku[1]))\
            * 60 + (int(self.seku[2]))
        self.second_input = self.lineEdit_2.text()

# Нахождение разницы между времяними
        if self.sekcur >= self.seknot or self.second_input == '':

            notification.notify(
                title='WARNING)',
                message='Your time is incorrect or gap is empty',
                app_icon='ph.ico',
                timeout=6,)

# Если введенное время раншье реальной, то программа выведет ошибку

        else:
            self.secs = 3600 * (int(self.seku2[0]) - int(self.seku[0]))\
                + 60 * (int(self.seku2[1]) - int(self.seku[1]))\
                - int(self.seku[2])

            notification.notify(
                title='Notification from iMAGA)',
                message='Your note was submitted, pls wait',
                app_icon='ph.ico',
                timeout=6,)

            t = time.sleep(int(self.secs))
            
            notification.notify(
                title='Notification from iMAGA)',
                message=self.second_input,
                app_icon='ph.ico',
                timeout=6,)

# Считывание количесво секунд через которое нужно будет сделать напоминание

    def bakk(self):
        self.close()
        self.nazad = MyWidget()
        self.nazad.show()

# Функция для возвращения на главную страницу

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

# Фрагмент для закрытие окон
