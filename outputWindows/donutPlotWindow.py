from PyQt4 import QtGui
import donutPlotLayout
from PIL import Image


class DonutPlotWindow(QtGui.QWidget, donutPlotLayout.Ui_donutPlot):
    def __init__(self, parent=None):
        super(DonutPlotWindow, self).__init__(parent)
        self.setupUi(self)

    def display_image(self):
        standardSize = Image.open("topologyDonut.png").size

        self.move(0, 600)
        self.donutPlotImage.setScaledContents(True)
        self.donutPlotImage.setPixmap(QtGui.QPixmap("topologyDonut.png"))
        self.resize(int(standardSize[0]), int(standardSize[1]))
