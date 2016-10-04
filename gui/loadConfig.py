# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadConfig.ui'
#
# Created: Tue Oct  4 12:50:20 2016
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
        Dialog.resize(872, 195)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(760, 160, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 851, 141))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 831, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.StopText = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.StopText.setObjectName(_fromUtf8("StopText"))
        self.horizontalLayout_4.addWidget(self.StopText)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.BusText = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.BusText.setObjectName(_fromUtf8("BusText"))
        self.horizontalLayout_2.addWidget(self.BusText)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dayStart = QtGui.QComboBox(self.verticalLayoutWidget)
        self.dayStart.setObjectName(_fromUtf8("dayStart"))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.dayStart.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.dayStart)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.dayEnd = QtGui.QComboBox(self.verticalLayoutWidget)
        self.dayEnd.setObjectName(_fromUtf8("dayEnd"))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.dayEnd.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.dayEnd)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.timeStart = QtGui.QComboBox(self.verticalLayoutWidget)
        self.timeStart.setObjectName(_fromUtf8("timeStart"))
        self.horizontalLayout_3.addWidget(self.timeStart)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.timeEnd = QtGui.QComboBox(self.verticalLayoutWidget)
        self.timeEnd.setObjectName(_fromUtf8("timeEnd"))
        self.horizontalLayout_3.addWidget(self.timeEnd)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.freq = QtGui.QComboBox(self.verticalLayoutWidget)
        self.freq.setObjectName(_fromUtf8("freq"))
        self.horizontalLayout_3.addWidget(self.freq)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "busAlert Configuration", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
        self.label.setText(_translate("Dialog", "Bus Stops", None))
        self.label_2.setText(_translate("Dialog", "Bus Lines", None))
        self.label_3.setText(_translate("Dialog", "Monitor bus", None))
        self.dayStart.setItemText(0, _translate("Dialog", "mon", None))
        self.dayStart.setItemText(1, _translate("Dialog", "tue", None))
        self.dayStart.setItemText(2, _translate("Dialog", "wed", None))
        self.dayStart.setItemText(3, _translate("Dialog", "thu", None))
        self.dayStart.setItemText(4, _translate("Dialog", "fri", None))
        self.dayStart.setItemText(5, _translate("Dialog", "sat", None))
        self.dayStart.setItemText(6, _translate("Dialog", "sun", None))
        self.label_4.setText(_translate("Dialog", "through", None))
        self.dayEnd.setItemText(0, _translate("Dialog", "mon", None))
        self.dayEnd.setItemText(1, _translate("Dialog", "tue", None))
        self.dayEnd.setItemText(2, _translate("Dialog", "wed", None))
        self.dayEnd.setItemText(3, _translate("Dialog", "thu", None))
        self.dayEnd.setItemText(4, _translate("Dialog", "fri", None))
        self.dayEnd.setItemText(5, _translate("Dialog", "sat", None))
        self.dayEnd.setItemText(6, _translate("Dialog", "sun", None))
        self.label_5.setText(_translate("Dialog", "from", None))
        self.label_6.setText(_translate("Dialog", "to", None))
        self.label_7.setText(_translate("Dialog", "every", None))
        self.label_8.setText(_translate("Dialog", "min", None))

