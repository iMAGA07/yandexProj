# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filebir.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 316)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"         border: 2px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: rgb(255, 170, 0);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(255, 170, 0);;\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.re_but = QtWidgets.QPushButton(self.centralwidget)
        self.re_but.setGeometry(QtCore.QRect(261, 130, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.re_but.setFont(font)
        self.re_but.setStyleSheet("QPushButton {\n"
"         border: 1.5px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: rgb(255, 170, 0);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(255, 170, 0);;\n"
"    \n"
"}")
        self.re_but.setObjectName("re_but")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 481, 91))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 201, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 209, 61, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 239, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 209, 84, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"         border: 1.5px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: rgb(255, 170, 0);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(255, 170, 0);;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RunProfit Launcher"))
        self.pushButton.setText(_translate("MainWindow", "Notepad"))
        self.re_but.setText(_translate("MainWindow", "Reminder"))
        self.label.setText(_translate("MainWindow", "RunProfit Launcher"))
        self.label_2.setText(_translate("MainWindow", "Your estimate from 1 to 10"))
        self.label_3.setText(_translate("MainWindow", "by iMAGA"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
