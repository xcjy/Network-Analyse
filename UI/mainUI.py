# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PlotCanvas import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = PlotCanvas(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)


        MainWindow.setMenuBar(self.menubar)
        self.NodeCount = QtWidgets.QLabel("节点:")
        self.EdgeCount = QtWidgets.QLabel("边:")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.addPermanentWidget(self.NodeCount, stretch=1)
        self.statusbar.addPermanentWidget(self.EdgeCount, stretch=1)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionrandom_graph = QtWidgets.QAction(MainWindow)
        self.actionrandom_graph.setObjectName("actionrandom_graph")
        self.actionsmall_world = QtWidgets.QAction(MainWindow)
        self.actionsmall_world.setObjectName("actionsmall_world")
        self.action_export = QtWidgets.QAction(MainWindow)
        self.action_export.setObjectName("action_export")
        self.actionregular_graph = QtWidgets.QAction(MainWindow)
        self.actionregular_graph.setCheckable(False)
        self.actionregular_graph.setObjectName("actionregular_graph")
        self.actiondegreeDis = QtWidgets.QAction(MainWindow)
        self.actiondegreeDis.setObjectName("actiondegreeDis")
        self.actiondeg_reeCentrality = QtWidgets.QAction(MainWindow)
        self.actiondeg_reeCentrality.setObjectName("actiondeg_reeCentrality")
        self.actiondegreeBetwenness = QtWidgets.QAction(MainWindow)
        self.actiondegreeBetwenness.setObjectName("actiondegreeBetwenness")
        self.actionBA = QtWidgets.QAction(MainWindow)
        self.actionBA.setObjectName("actionBA")
        self.actionClosenessCentrality = QtWidgets.QAction(MainWindow)
        self.actionClosenessCentrality.setObjectName("actionClosenessCentrality")
        self.actionClustering = QtWidgets.QAction(MainWindow)
        self.actionClustering.setObjectName("actionClustering")
        self.actionAverage_shortest_path_length = QtWidgets.QAction(MainWindow)
        self.actionAverage_shortest_path_length.setObjectName("actionAverage_shortest_path_length")
        self.actionNodeLable = QtWidgets.QAction(MainWindow)
        self.actionNodeLable.setObjectName("actionNodeLable")


        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.action_export)
        self.menu_2.addAction(self.actionregular_graph)
        self.menu_2.addAction(self.actionrandom_graph)
        self.menu_2.addAction(self.actionsmall_world)
        self.menu_2.addAction(self.actionBA)
        self.menu_3.addAction(self.actiondegreeDis)
        self.menu_3.addAction(self.actiondeg_reeCentrality)
        self.menu_3.addAction(self.actiondegreeBetwenness)
        self.menu_3.addAction(self.actionClosenessCentrality)
        self.menu_3.addAction(self.actionClustering)
        self.menu_3.addAction(self.actionAverage_shortest_path_length)

        self.menu_4.addAction(self.actionNodeLable)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "生成"))
        self.menu_3.setTitle(_translate("MainWindow", "分析指标"))
        self.menu_4.setTitle(_translate("MainWindow", "样式"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionrandom_graph.setText(_translate("MainWindow", "ER随机图"))
        self.actionsmall_world.setText(_translate("MainWindow", "WS小世界网络"))
        self.action_export.setText(_translate("MainWindow", "导出"))
        self.actionregular_graph.setText(_translate("MainWindow", "规则图"))
        self.actiondegreeDis.setText(_translate("MainWindow", "度分布"))
        self.actiondeg_reeCentrality.setText(_translate("MainWindow", "度中心性"))
        self.actiondegreeBetwenness.setText(_translate("MainWindow", "介数中心性"))
        self.actionBA.setText(_translate("MainWindow", "BA无标度网络"))
        self.actionClosenessCentrality.setText(_translate("MainWindow", "紧密中心性"))
        self.actionClustering.setText(_translate("MainWindow", "平均群聚系数"))
        self.actionAverage_shortest_path_length.setText(_translate("MainWindow", "平均最短距离"))
        self.actionNodeLable.setText(_translate("MainWindow", "显示节点标签 "))



