# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomGraphUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class RandomGraphDialogUi(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 225)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-70, 150, 331, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Node = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Node.setGeometry(QtCore.QRect(110, 30, 113, 21))
        self.lineEdit_Node.setObjectName("lineEdit_Node")
        self.lineEdit_p = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_p.setGeometry(QtCore.QRect(110, 70, 113, 21))
        self.lineEdit_p.setObjectName("lineEdit_p")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "节点数："))
        self.label_2.setText(_translate("Dialog", "连线的概率："))

