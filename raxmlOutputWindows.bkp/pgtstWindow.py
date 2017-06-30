from PyQt4 import QtGui, QtCore
import pgtstLayout
from PIL import Image
import sys, os
from shutil import copyfile


class PGTSTWindow(QtGui.QMainWindow, pgtstLayout.Ui_pgtst):
    def __init__(self, parent=None):
        super(PGTSTWindow, self).__init__(parent)
        self.setupUi(self)

        self.fileName = 'PGTSTPlot.png'

        # moves menu bar into application -- mac only windows sux
        self.menubar.setNativeMenuBar(False)

        # bind export actions
        self.actionPNG.triggered.connect(lambda: self.exportFile(self.fileName))
        self.actionPDF.triggered.connect(lambda: self.exportFile(self.fileName))

    def display_image(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)

        pgtstPlotSize = Image.open(self.fileName).size

        self.move(1000, 0)
        self.pgtstImage.setScaledContents(True)
        self.pgtstImage.setPixmap(QtGui.QPixmap(self.fileName))
        self.resize(int(pgtstPlotSize[0]), int(pgtstPlotSize[1]))

    def exportFile(self, fileName):
        extension = os.path.splitext(fileName)[1]
        name = QtGui.QFileDialog.getSaveFileName(self, 'Export ' + extension[1:]) + extension
        copyfile(fileName, name)

# if you want to test LOCALLY change the path to PGTSTPlot.png #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':  # if we're running file directly and not importing it
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication

    # initialize main input window
    form = PGTSTWindow()  # We set the form to be our PhyloVisApp (design)
    form.show()  # Show the form
    form.display_image()

    sys.exit(app.exec_())  # and execute the app