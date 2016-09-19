# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created: Sun Sep 18 18:48:35 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(595, 330)
        self.StopText = QtGui.QTextEdit(Dialog)
        self.StopText.setGeometry(QtCore.QRect(20, 40, 531, 78))
        self.StopText.setObjectName(_fromUtf8("StopText"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BusText = QtGui.QTextEdit(Dialog)
        self.BusText.setGeometry(QtCore.QRect(20, 170, 531, 78))
        self.BusText.setObjectName(_fromUtf8("BusText"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 280, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "BusAlert", None))
        self.label.setText(_translate("Dialog", "Bus Stops", None))
        self.label_2.setText(_translate("Dialog", "Bus Lines", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))

