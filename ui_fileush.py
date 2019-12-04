from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 286)
        Form.setStyleSheet("background-color: #ff7142;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(6, 90, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(7, 134, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(322, 140, 71, 20))
        self.lineEdit_2.setStyleSheet("color #ff7142;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"         border: 2px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: #c8c8c8;;\n"
"         min-width: 80px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: #c8c8c8;;\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"         border: 2px solid #000000;\n"
"         border-radius :8px;\n"
"         color: #000000;\n"
"         background-color: #c8c8c8;;\n"
"         min-width: 20px;\n"
"     }\n"
"\n"
"QPushButton:pressed {\n"
"         background-color: #c8c8c8;;\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tm = QtWidgets.QTimeEdit(Form)
        self.tm.setGeometry(QtCore.QRect(331, 100, 61, 22))
        self.tm.setObjectName("tm")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REMINDER"))
        self.label.setText(_translate("Form", "when do u want to be reminded?"))
        self.label_2.setText(_translate("Form", "what do u want to be reminded?"))
        self.label_3.setText(_translate("Form", "REMINDER"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label_4.setText(_translate("Form", "      by iMAGA"))
        self.pushButton_2.setText(_translate("Form", "Back"))
