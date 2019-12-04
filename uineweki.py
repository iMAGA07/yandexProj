from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 306)
        Form.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 259, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #75b8ff")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 37, 84, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"         color: #ffdb6f;\n"
"         background-color: rgb(64, 64, 64);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(64, 64, 64);;\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(152, 37, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"         color: #ffdb6f;\n"
"         background-color: rgb(64, 64, 64);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(64, 64, 64);;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 37, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"         color: #ffdb6f;\n"
"         background-color: rgb(64, 64, 64);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(64, 64, 64);;\n"
"    \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.NOTEPAD = QtWidgets.QLabel(Form)
        self.NOTEPAD.setGeometry(QtCore.QRect(158, 9, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(12)
        self.NOTEPAD.setFont(font)
        self.NOTEPAD.setStyleSheet("color: #75b8ff;")
        self.NOTEPAD.setObjectName("NOTEPAD")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 264, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"         color: #ffdb6f;\n"
"         background-color: rgb(64, 64, 64);;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: rgb(64, 64, 64);;\n"
"    \n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 66, 381, 191))
        self.plainTextEdit.setStyleSheet("background-color: #ffdb6f;")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "NOTEPAD"))
        self.label.setText(_translate("Form", "by iMAGA"))
        self.pushButton.setText(_translate("Form", "Open file"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.pushButton_3.setText(_translate("Form", "Save as"))
        self.NOTEPAD.setText(_translate("Form", "NOTEPAD"))
        self.pushButton_4.setText(_translate("Form", "Back"))
