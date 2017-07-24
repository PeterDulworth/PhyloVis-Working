from standardWindow import Window
from PyQt4 import QtGui
import sys

"""
Functions:
    __init__(self)
~
Chabrielle Allen
Travis Benedict
Peter Dulworth
"""


class AllTreesWindow(Window):
    def __init__(self):
        Window.__init__(self, windowTitle='All Trees Window')


if __name__ == '__main__':
    # test window if running locally
    app = QtGui.QApplication(sys.argv)
    form = AllTreesWindow()
    form.show()
    form.display_image()
    sys.exit(app.exec_())
