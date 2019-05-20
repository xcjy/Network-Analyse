# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baGraphDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class BaGraphDialogUI(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(286, 226)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 111, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lineEdit_Edge = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Edge.setGeometry(QtCore.QRect(150, 80, 113, 21))
        self.lineEdit_Edge.setObjectName("lineEdit_Edge")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Node = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Node.setGeometry(QtCore.QRect(150, 40, 113, 21))
        self.lineEdit_Node.setObjectName("lineEdit_Node")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "节点数："))
        self.label_2.setText(_translate("Dialog", "每次加入边数："))


