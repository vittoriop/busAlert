# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadConfig.ui'
#
# Created: Tue Sep 20 15:26:59 2016
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
        Dialog.resize(769, 208)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(640, 160, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.StopText = QtGui.QLineEdit(Dialog)
        self.StopText.setGeometry(QtCore.QRect(100, 20, 521, 21))
        self.StopText.setObjectName(_fromUtf8("StopText"))
        self.BusText = QtGui.QLineEdit(Dialog)
        self.BusText.setGeometry(QtCore.QRect(100, 70, 521, 21))
        self.BusText.setObjectName(_fromUtf8("BusText"))
        self.dayStart = QtGui.QComboBox(Dialog)
        self.dayStart.setGeometry(QtCore.QRect(100, 120, 81, 22))
        self.dayStart.setObjectName(_fromUtf8("dayStart"))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayEnd = QtGui.QComboBox(Dialog)
        self.dayEnd.setGeometry(QtCore.QRect(250, 120, 81, 22))
        self.dayEnd.setObjectName(_fromUtf8("dayEnd"))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.timeStart = QtGui.QComboBox(Dialog)
        self.timeStart.setGeometry(QtCore.QRect(380, 120, 81, 22))
        self.timeStart.setObjectName(_fromUtf8("timeStart"))
        self.timeEnd = QtGui.QComboBox(Dialog)
        self.timeEnd.setGeometry(QtCore.QRect(490, 120, 81, 22))
        self.timeEnd.setObjectName(_fromUtf8("timeEnd"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 120, 58, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 120, 58, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(470, 120, 58, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(580, 120, 58, 15))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(710, 120, 58, 15))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.freq = QtGui.QComboBox(Dialog)
        self.freq.setGeometry(QtCore.QRect(620, 120, 81, 22))
        self.freq.setObjectName(_fromUtf8("freq"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "BusAlert", None))
        self.label.setText(_translate("Dialog", "Bus Stops", None))
        self.label_2.setText(_translate("Dialog", "Bus Lines", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
        self.dayStart.setItemText(0, _translate("Dialog", "Mon", None))
        self.dayStart.setItemText(1, _translate("Dialog", "Tue", None))
        self.dayStart.setItemText(2, _translate("Dialog", "Wed", None))
        self.dayStart.setItemText(3, _translate("Dialog", "Thu", None))
        self.dayStart.setItemText(4, _translate("Dialog", "Fri", None))
        self.dayStart.setItemText(5, _translate("Dialog", "Sat", None))
        self.dayStart.setItemText(6, _translate("Dialog", "Sun", None))
        self.dayEnd.setItemText(0, _translate("Dialog", "Mon", None))
        self.dayEnd.setItemText(1, _translate("Dialog", "Tue", None))
        self.dayEnd.setItemText(2, _translate("Dialog", "Wed", None))
        self.dayEnd.setItemText(3, _translate("Dialog", "Thu", None))
        self.dayEnd.setItemText(4, _translate("Dialog", "Fri", None))
        self.dayEnd.setItemText(5, _translate("Dialog", "Sat", None))
        self.dayEnd.setItemText(6, _translate("Dialog", "Sun", None))
        self.label_3.setText(_translate("Dialog", "Monitor bus", None))
        self.label_4.setText(_translate("Dialog", "through", None))
        self.label_5.setText(_translate("Dialog", "from", None))
        self.label_6.setText(_translate("Dialog", "to", None))
        self.label_7.setText(_translate("Dialog", "every", None))
        self.label_8.setText(_translate("Dialog", "min", None))

