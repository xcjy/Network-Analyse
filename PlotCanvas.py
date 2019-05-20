import networkx as nx
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets

# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=800, height=600, dpi=100):
        # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig=fig
        # 调用父类的构造函数
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        #设置尺寸为QtWigets的尺寸
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


