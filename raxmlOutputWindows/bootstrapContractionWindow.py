from window import Window
from PyQt4 import QtGui
import sys


if __name__ == '__main__':
    fileName = '../ContractedGraph.png'
else:
    fileName = 'ContractedGraph.png'


class BootstrapContractionWindow(Window):
    def __init__(self):
        Window.__init__(self, fileName, x=40, y=62, scale=3)

if __name__ == '__main__':
    # test window if running locally
    app = QtGui.QApplication(sys.argv)
    form = BootstrapContractionWindow()
    form.show()
    form.display_image()
    sys.exit(app.exec_())