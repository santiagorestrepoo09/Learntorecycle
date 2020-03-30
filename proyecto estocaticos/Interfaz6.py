# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interfaz7.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resource

class Ui_Form6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(799, 446)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 451))
        self.label.setStyleSheet("border-image: url(:/newPrefix/fondo.qrc.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 711, 401))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 691, 381))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 691, 61))
        self.label_4.setStyleSheet("border-image: url(:/newPrefix/superio.png);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 90, 661, 301))
        self.label_5.setStyleSheet("border-image: url(:/newPrefix/fondoex.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 61, 51))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/return.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 360, 61, 51))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/confirmar.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Learn to recycle </span></p></body></html>"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form6 = QtWidgets.QMainWindow()
    ui = Ui_Form6()
    ui.setupUi(Form6)
    Form6.show()
    sys.exit(app.exec_())  