import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog

from UI.randomGraphDialogUi import RandomGraphDialogUi
from UI.regularGraphDialog import RegularGraphDialogUi
from UI.baGraphDialog import BaGraphDialogUI
from UI.WsGraphDialog import WsGraphDialogUi
from UI.mainUI import Ui_MainWindow
import networkx as nx
import numpy as np
import math
from scipy import linalg
import matplotlib.pyplot as plt

#对话框
class RandomGraphDialog( RandomGraphDialogUi):
    def __init__(self):
        super( RandomGraphDialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("生成随机图")
    #确认按钮
    def accept(self):
        Nodes=self.lineEdit_Node.text()
        p=self.lineEdit_p.text()
        myWin.drawErRandom(int(Nodes),float(p))
        self.close()
class RegularGraphDialog(RegularGraphDialogUi):
    def __init__(self):
        super(RegularGraphDialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("生成规则图")
        # 确认按钮

    def accept(self):
        Nodes = self.lineEdit_Node.text()
        Neighbour = self.lineEdit_Neighbour.text()
        myWin.drawRegularGraph(int(Neighbour), int(Nodes))
        self.close()
class WsGraphDialog(WsGraphDialogUi):
    def __init__(self):
        super(WsGraphDialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("生成WS小世界网络")
    def accept(self):
        Nodes = self.lineEdit_Node.text()
        Neighbour = self.lineEdit_Neighbour.text()
        p=self.lineEdit_p.text()
        myWin.drawWsGraph(int(Nodes), int(Neighbour),float(p))
        self.close()
class BaGraphDialog(BaGraphDialogUI):
    def __init__(self):
        super(BaGraphDialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("生成BA无标度网络")
    def accept(self):
        Node=self.lineEdit_Node.text()
        Edges=self.lineEdit_Edge.text()
        myWin.drawBaGraph(int(Node),int(Edges))


#主窗口
class MyWindow(QMainWindow,Ui_MainWindow):
    #构造函数
    def __init__(self, parent=None):
        #调用父亲的构造函数
        super(MyWindow, self).__init__(parent)
        # 更新current Graph 当前的网络
        self.currentGraph = nx.Graph()
        self.DisplayNodeLable=False
        #调用父类的setupUi
        self.setupUi(self)
        self.setWindowTitle("网络特征分析")

        #初始化Dialog窗口
        self.randomGraphDialog=RandomGraphDialog()
        self.regulrGraphDialog=RegularGraphDialog()
        self.baGraphDialog=BaGraphDialog()
        self.wsGraphDialog=WsGraphDialog()
        #绑定Dialog 槽函数
        self.actionrandom_graph.triggered.connect(self.randomGraphDialog.show)
        self.actionregular_graph.triggered.connect(self.regulrGraphDialog.show)
        self.actionBA.triggered.connect(self.baGraphDialog.show)
        self.actionsmall_world.triggered.connect(self.wsGraphDialog.show)
        #绑定分析指标 槽函数
        self.actiondegreeDis.triggered.connect(self.drawDegreeDis)
        self.actiondeg_reeCentrality.triggered.connect(self.drawDegreeCentrality)
        self.actiondegreeBetwenness.triggered.connect(self.drawBetweennessCentrality)
        self.actionClosenessCentrality.triggered.connect(self.drawClosenessCentrality)
        self.actionClustering.triggered.connect(self.drawAverageClustering)
        self.actionAverage_shortest_path_length.triggered.connect(self.drawAverage_short_path)
        self.actionNodeLable.triggered.connect(self.ShowNodeLable)

        #绑定打开、导出 槽函数
        self.actionopen.triggered.connect(self.openFile)
        self.action_export.triggered.connect(self.exportFile)


    def drawDegreeDis(self):
         G=self.currentGraph
         degree = nx.degree_histogram(G)  # 返回图中从1到最大度的出现频次
     #    print(G.degree())
     #    print(len(degree))
         x = range( len(degree))  # 生成X轴序列，从1到最大度
         print(x)
         y = [z / float(sum(degree)) for z in degree]  # 将频次转化为频率，利用列表内涵
         print(y)
         plt.loglog(x, y, color="blue", linewidth=2)  # 在双对坐标轴上绘制度分布曲线
       #  plt.scatter(x,y,color="blue",linewidth=2)
       #
       #   dict_=dict(G.degree())
       #   print(dict_)
       #   values=list(dict_.values())
       #   print(values)
       #   import seaborn as sns
       #   import pandas as pd
       #   a=pd.Series(values)
       #   print(a)
       #   sns.distplot(a)

       #  print(values.max())
       #  plt.xlim(0,values.max())
         plt.xlabel('Degree')
         plt.ylabel('Probability')
         plt.title("Degree Distribution")
         plt.show()  # 显示图表

    def drawDegreeCentrality(self):
        print("draw centrality")
        G=self.currentGraph
        c=nx.degree_centrality(G)
        plt.bar(c.keys(),c.values())
        plt.xlabel("Node")
        plt.ylabel("Degree centrality")
        plt.show()

    def drawBetweennessCentrality(self):
        print("draw betweenness")
        G=self.currentGraph
        c=nx.centrality.betweenness_centrality(G)
        plt.bar(c.keys(), c.values())
        plt.xlabel("Node")
        plt.ylabel("Betweenness centrality")
        plt.show()
    def drawClosenessCentrality(self):
        print("draw close")
        G=self.currentGraph
        c=nx.centrality.closeness_centrality(G)
        plt.bar(c.keys(),c.values())
        plt.xlabel("Node")
        plt.ylabel("Closeness Centrality")
        plt.show()

    def drawAverageClustering(self):
        print("clustering")
        G=self.currentGraph
        print( nx.average_clustering(G)  )
    def drawAverage_short_path(self):
        print(nx.average_shortest_path_length(self.currentGraph))

    def ShowNodeLable(self):
        print("shownodelable")
        if(self.DisplayNodeLable==False):
            self.DisplayNodeLable=True
        else:
            self.DisplayNodeLable=False
        self.refresh()
        print(self.DisplayNodeLable)
        nx.draw(self.currentGraph,pos=nx.spring_layout(self.currentGraph),
                ax=self.axes, with_labels=self.DisplayNodeLable,node_size=30)


    def refresh(self):
               self.axes = self.widget.fig.add_subplot(111)
               self.axes.cla()
               self.widget.fig.canvas.draw_idle()

    def refreshStatusBar(self):
        # 更新状态栏
        self.NodeCount.setText("节点:" + str(self.currentGraph.number_of_nodes()))
        self.EdgeCount.setText("边:" + str(self.currentGraph.number_of_edges()))

    def openFile(self):
            try:
                fileName = QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                                                                 'Graph Files(*.gml , *.gpickle , *.gexf)'
                                                                 )  # 第三个参数设置文件扩展名过滤,
                print(fileName[0])  # 0是路径
                self.readGraph(fileName[0])
            except Exception as e:
                print(e)

    def exportFile(self):
            try:
                fileName = QFileDialog.getSaveFileName(self,
                                                                 "文件保存", "C:/",
                                                                 'Graph Files(*.gml , *.gpickle , *.gexf)')
                #获取导出文件路径
                path = fileName[0]
                #获取文件后缀名
                suf = os.path.splitext(path)[-1]
                if suf == ".gml":
                    nx.readwrite.write_gml(self.currentGraph, fileName[0])
                elif suf == ".gexf":
                    nx.readwrite.write_gexf(self.currentGraph, fileName[0])
                elif suf == ".gpickle":
                    nx.readwrite.write_gpickle(self.currentGraph, fileName[0])
            except Exception as e:  #捕获异常
                print(e)

    def readGraph(self, path):
            # 判断后缀名
            suf = os.path.splitext(path)[-1]
            if suf == ".gml":
                G = nx.readwrite.read_gml(path)
            elif suf == ".gexf":
                G = nx.readwrite.read_gexf(path)
            elif suf == ".gpickle":
                G = nx.readwrite.read_gpickle(path)
            #选择布局算法
            pos = nx.spring_layout(G)
            #更新当前图
            self.currentGraph = G
            #刷新界面
            self.refresh()
            nx.draw(G, pos, ax=self.axes, with_labels=self.DisplayNodeLable, node_size=10, alpha=1)
            #刷新状态栏
            self.refreshStatusBar()

    def drawErRandom(self, node, p):

            ER = nx.random_graphs.erdos_renyi_graph(node, p)
            self.currentGraph = ER
            self.refresh()

            # 设置布局
            pos = nx.shell_layout(ER)
            nx.draw(ER, pos, node_color='r', ax=self.axes,
                    edge_color='black', with_labels=self.DisplayNodeLable, alpha=1,
                    font_size=10, node_size=20, arrows=True)
            self.refreshStatusBar()


    def drawRegularGraph(self, neighbour, node):
            self.refresh()

            RG =   nx.random_graphs.watts_strogatz_graph(node, neighbour, 0)

            self.currentGraph = RG
            # 设置布局
            pos = nx.shell_layout(RG)
            nx.draw(RG, pos, ax=self.axes, with_labels=self.DisplayNodeLable, node_size=30)
            self.refreshStatusBar()

        # 用random_graphs.watts_strogatz_graph(n, k, p)方法生成一个含有n个节点、每个节点有k个邻居、以概率p随机化重连边的WS小世界网络。
    def drawWsGraph(self, node, neighbour, p):
            self.refresh()
            WS = nx.random_graphs.watts_strogatz_graph(node, neighbour, p)
            self.currentGraph = WS
            pos = nx.circular_layout(WS)
            nx.draw(WS, pos, ax=self.axes, with_labels=self.DisplayNodeLable, node_size=30)
            self.refreshStatusBar()

        #  n个节点 每次加入m条边的无标度网络
    def drawBaGraph(self, node, edge):
            self.refresh()
            BA = nx.random_graphs.barabasi_albert_graph(node, edge)
            self.currentGraph = BA
            pos = nx.spring_layout(BA)
         #   pos=nx.kamada_kawai_layout(BA)
            nx.draw(BA, pos, ax=self.axes, with_labels=self.DisplayNodeLable, node_size=30)
            self.refreshStatusBar()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow() #定义主窗口
    myWin.show()  #显示主窗口
    sys.exit(app.exec_())


