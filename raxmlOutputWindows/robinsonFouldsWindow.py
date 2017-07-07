from tabWindow import TabWindow
from PyQt4 import QtGui
import sys

if __name__ == '__main__':
    unweightedFileName = '../plots/UnweightedFouldsPlot.png'
    weightedFileName = '../plots/WeightedFouldsPlot.png'
else:
    unweightedFileName = 'plots/UnweightedFouldsPlot.png'
    weightedFileName = 'plots/WeightedFouldsPlot.png'


class RobinsonFouldsWindow(TabWindow):
    def __init__(self):
        TabWindow.__init__(self, unweightedFileName, weightedFileName, x=200, y=222, scale=1) #!!! add ../ before file name to test locally


if __name__ == '__main__':
    # test window if running locally
    app = QtGui.QApplication(sys.argv)
    form = RobinsonFouldsWindow()
    form.show()
    form.displayImages()
    sys.exit(app.exec_())
