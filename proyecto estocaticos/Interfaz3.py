# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interfaz4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resource


class Ui_Form3(object):
    
    def openWindow(self):
        from Interfaz4 import Ui_Form4
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form4()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow2(self):
        from Interfaz5 import Ui_Form5
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form5()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow3(self):
        from Interfaz6 import Ui_Form6
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form6()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow4(self):
        from Interfaz2 import Ui_Form1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(859, 408)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 871, 411))
        self.label.setStyleSheet("image: url(:/newPrefix/fondogrande.png);\n"
"border-image: url(:/newPrefix/fondogrande.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 741, 331))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 161, 311))
        self.label_3.setStyleSheet("background-color: rgb(145, 145, 145);\n"
"background-color: rgb(118, 118, 118);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 40, 561, 311))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 40, 561, 51))
        self.label_5.setStyleSheet("image: url(:/newPrefix/superio.png);\n"
"border-image: url(:/newPrefix/superio.png);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 140, 171, 111))
        self.pushButton.setStyleSheet("\n"
"border-image: url(:/newPrefix/boton1.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 140, 171, 111))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/boton2.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 40, 61, 51))
        self.label_6.setStyleSheet("border-image: url(:/newPrefix/user.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(160, 50, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(100, 100, 121, 31))
        self.label_8.setStyleSheet("border-image: url(:/newPrefix/location.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(100, 180, 121, 31))
        self.label_9.setStyleSheet("border-image: url(:/newPrefix/Direction.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(100, 260, 121, 31))
        self.label_10.setStyleSheet("border-image: url(:/newPrefix/postal.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 140, 131, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 220, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 300, 131, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 140, 171, 111))
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/boton rojo.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 300, 61, 51))
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/exit.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton.clicked.connect(self.openWindow)     
        self.pushButton_2.clicked.connect(self.openWindow2)   
        self.pushButton_3.clicked.connect(self.openWindow3)   
        self.pushButton_4.clicked.connect(self.openWindow4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Learn to recycle </span></p></body></html>"))
        self.label_7.setText(_translate("Form", "Name"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form3 = QtWidgets.QMainWindow()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())  