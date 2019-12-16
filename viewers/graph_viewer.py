from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget
import pyqtgraph

import nv_utils.utils as utils
from nv_utils.singleton import Singleton

class GraphViewer(QDockWidget, metaclass=Singleton):
    def __init__(self, parent):
        super(GraphViewer, self).__init__(parent)

        self.plot_widget = PlotWidget()
        self.plot_widget.setRenderHint(QPainter.HighQualityAntialiasing)
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setMenuEnabled(False)

        self.setWidget(self.plot_widget)

        self.setParent(parent)
        self.setWindowTitle("Graph Viewer")
        self.setFloating(True)

        self.set_background_color(QColor(42, 42, 42))

    def set_background_color(self, qcolor):
        self.plot_widget.setBackground(qcolor)

    def plot(self, plot_object):
        title = plot_object.get_title()
        x_axis_title = plot_object.get_x_axis_title()
        y_axis_title = plot_object.get_y_axis_title()
        x_axis = plot_object.get_x_axis_values()
        y_axis = plot_object.get_y_axis_values()
        pen = plot_object.get_pen()
        marker_shape = plot_object.get_marker_shape()
        marker_size = plot_object.get_marker_size()
        marker_color = plot_object.get_marker_color()
        marker_pen = plot_object.get_marker_pen()

        self.plot_widget.setTitle(title)
        self.plot_widget.setLabel("left", y_axis_title)
        self.plot_widget.setLabel("bottom", x_axis_title)

        if plot_object.get_clear_first():
            self.clear()

        if plot_object.get_show_markers():
            self.plot_widget.plot(x_axis, y_axis, pen=pen, symbol=marker_shape, symbolSize=marker_size, symbolBrush=marker_color, symbolPen=marker_pen,)
        else:
            self.plot_widget.plot(x_axis, y_axis, pen=pen)

    def clear(self):
        self.plot_widget.getPlotItem().clear()

    def resizeEvent(self, event):
        super().resizeEvent(event)




