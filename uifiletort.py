from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 376)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 0, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 70, 411, 241))
        self.plainTextEdit.setStyleSheet("background-color: rgb(149, 215, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 340, 84, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"         border: 2px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: #ffff7f;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: #ffff7f;\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 320, 54, 20))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"         border: 2px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: #ffff7f;\n"
"         min-width: 50px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: #ffff7f;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please, write your recommendation to improve"))
        self.label_2.setText(_translate("Form", " my program"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.pushButton_2.setText(_translate("Form", "Back"))
