from PyQt4 import QtGui, QtCore
import scatterPlotLayout
from PIL import Image
import sys, os
from shutil import copyfile


class ScatterPlotWindow(QtGui.QMainWindow, scatterPlotLayout.Ui_scatterPlot):
    def __init__(self, parent=None):
        super(ScatterPlotWindow, self).__init__(parent)
        self.setupUi(self)

        self.fileName = 'topologyScatter.png'

        # moves menu bar into application -- mac only windows sux
        self.menubar.setNativeMenuBar(False)

        # bind export actions
        self.actionPNG.triggered.connect(lambda: self.exportFile(self.fileName))
        self.actionPDF.triggered.connect(lambda: self.exportFile(self.fileName))

    def display_image(self):
        # change background color to white
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)

        # get size of image
        standardSize = Image.open(self.fileName).size

        # move, display and resize window
        self.move(800, 600)
        self.scatterPlotImage.setScaledContents(True)
        self.scatterPlotImage.setPixmap(QtGui.QPixmap(self.fileName))
        self.resize(int(standardSize[0]), int(standardSize[1]))

    def exportFile(self, fileName):
        extension = os.path.splitext(fileName)[1]
        name = QtGui.QFileDialog.getSaveFileName(self, 'Export ' + extension[1:]) + extension
        copyfile(fileName, name)

# if you want to test LOCALLY change the path to ../Topology0.png #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':  # if we're running file directly and not importing it
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication

    # initialize main input window
    form = ScatterPlotWindow()  # We set the form to be our PhyloVisApp (design)
    form.show()  # Show the form
    form.display_image()

    sys.exit(app.exec_())  # and execute the app