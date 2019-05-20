# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WsGraphDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class WsGraphDialogUi(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(308, 224)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 111, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lineEdit_Neighbour = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Neighbour.setGeometry(QtCore.QRect(130, 70, 113, 21))
        self.lineEdit_Neighbour.setObjectName("lineEdit_Neighbour")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Node = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Node.setGeometry(QtCore.QRect(130, 30, 113, 21))
        self.lineEdit_Node.setObjectName("lineEdit_Node")
        self.lineEdit_p = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_p.setGeometry(QtCore.QRect(130, 110, 113, 21))
        self.lineEdit_p.setObjectName("lineEdit_p")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 91, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "节点数："))
        self.label_2.setText(_translate("Dialog", "邻居节点数："))
        self.label_3.setText(_translate("Dialog", "连线的概率："))


