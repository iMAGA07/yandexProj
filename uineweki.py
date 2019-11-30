# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uineweki.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(205, 220, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 270, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(41, 33, 71, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(122, 33, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(192, 33, 56, 17))
        self.pushButton_3.setObjectName("pushButton_3")
        self.NOTEPAD = QtWidgets.QLabel(Form)
        self.NOTEPAD.setGeometry(QtCore.QRect(160, -1, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.NOTEPAD.setFont(font)
        self.NOTEPAD.setObjectName("NOTEPAD")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 270, 71, 17))
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(43, 83, 311, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                     by iMAGA"))
        self.pushButton.setText(_translate("Form", "Open file"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.pushButton_3.setText(_translate("Form", "Save as"))
        self.NOTEPAD.setText(_translate("Form", "NOTEPAD"))
        self.pushButton_4.setText(_translate("Form", "Back"))
