# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_layout.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PhylogeneticVisualization(object):
    def setupUi(self, PhylogeneticVisualization):
        PhylogeneticVisualization.setObjectName(_fromUtf8("PhylogeneticVisualization"))
        PhylogeneticVisualization.resize(433, 170)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhylogeneticVisualization.sizePolicy().hasHeightForWidth())
        PhylogeneticVisualization.setSizePolicy(sizePolicy)
        PhylogeneticVisualization.setMinimumSize(QtCore.QSize(433, 170))
        self.centralwidget = QtGui.QWidget(PhylogeneticVisualization)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inputMainHorizontalLayout = QtGui.QHBoxLayout()
        self.inputMainHorizontalLayout.setObjectName(_fromUtf8("inputMainHorizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.inputPage = QtGui.QWidget()
        self.inputPage.setObjectName(_fromUtf8("inputPage"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.inputPage)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.inputFileBtn = QtGui.QPushButton(self.inputPage)
        self.inputFileBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.inputFileBtn.setObjectName(_fromUtf8("inputFileBtn"))
        self.horizontalLayout_7.addWidget(self.inputFileBtn)
        self.inputFileEntry = QtGui.QLineEdit(self.inputPage)
        self.inputFileEntry.setMinimumSize(QtCore.QSize(0, 21))
        self.inputFileEntry.setMouseTracking(True)
        self.inputFileEntry.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.inputFileEntry.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.inputFileEntry.setObjectName(_fromUtf8("inputFileEntry"))
        self.horizontalLayout_7.addWidget(self.inputFileEntry)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.windowSizeLabel = QtGui.QLabel(self.inputPage)
        self.windowSizeLabel.setObjectName(_fromUtf8("windowSizeLabel"))
        self.horizontalLayout_8.addWidget(self.windowSizeLabel)
        self.windowSizeEntry = QtGui.QLineEdit(self.inputPage)
        self.windowSizeEntry.setMinimumSize(QtCore.QSize(40, 21))
        self.windowSizeEntry.setMaximumSize(QtCore.QSize(80, 16777215))
        self.windowSizeEntry.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.windowSizeEntry.setObjectName(_fromUtf8("windowSizeEntry"))
        self.horizontalLayout_8.addWidget(self.windowSizeEntry)
        self.windowOffsetLabel = QtGui.QLabel(self.inputPage)
        self.windowOffsetLabel.setObjectName(_fromUtf8("windowOffsetLabel"))
        self.horizontalLayout_8.addWidget(self.windowOffsetLabel)
        self.windowOffsetEntry = QtGui.QLineEdit(self.inputPage)
        self.windowOffsetEntry.setMinimumSize(QtCore.QSize(40, 21))
        self.windowOffsetEntry.setMaximumSize(QtCore.QSize(80, 16777215))
        self.windowOffsetEntry.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.windowOffsetEntry.setObjectName(_fromUtf8("windowOffsetEntry"))
        self.horizontalLayout_8.addWidget(self.windowOffsetEntry)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.runBtn = QtGui.QPushButton(self.inputPage)
        self.runBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.horizontalLayout_10.addWidget(self.runBtn)
        self.progressBar = QtGui.QProgressBar(self.inputPage)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_10.addWidget(self.progressBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.inputPage)
        self.inputPageNotRaxA = QtGui.QWidget()
        self.inputPageNotRaxA.setObjectName(_fromUtf8("inputPageNotRaxA"))
        self.gridLayout_2 = QtGui.QGridLayout(self.inputPageNotRaxA)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.inputPageNotRaxA)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.inputPageNotRaxA)
        self.lcdNumber.setProperty("intValue", 420)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.inputPageNotRaxA)
        self.inputPageNotRaxB = QtGui.QWidget()
        self.inputPageNotRaxB.setObjectName(_fromUtf8("inputPageNotRaxB"))
        self.label_2 = QtGui.QLabel(self.inputPageNotRaxB)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 56, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.stackedWidget.addWidget(self.inputPageNotRaxB)
        self.inputPageNotRaxC = QtGui.QWidget()
        self.inputPageNotRaxC.setObjectName(_fromUtf8("inputPageNotRaxC"))
        self.label_3 = QtGui.QLabel(self.inputPageNotRaxC)
        self.label_3.setGeometry(QtCore.QRect(180, 70, 56, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.stackedWidget.addWidget(self.inputPageNotRaxC)
        self.outputPage = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPage.sizePolicy().hasHeightForWidth())
        self.outputPage.setSizePolicy(sizePolicy)
        self.outputPage.setObjectName(_fromUtf8("outputPage"))
        self.gridLayout_5 = QtGui.QGridLayout(self.outputPage)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.outputTabs = QtGui.QTabWidget(self.outputPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTabs.sizePolicy().hasHeightForWidth())
        self.outputTabs.setSizePolicy(sizePolicy)
        self.outputTabs.setObjectName(_fromUtf8("outputTabs"))
        self.standard = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standard.sizePolicy().hasHeightForWidth())
        self.standard.setSizePolicy(sizePolicy)
        self.standard.setObjectName(_fromUtf8("standard"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.standard)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.standardImage = QtGui.QLabel(self.standard)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standardImage.sizePolicy().hasHeightForWidth())
        self.standardImage.setSizePolicy(sizePolicy)
        self.standardImage.setText(_fromUtf8(""))
        self.standardImage.setObjectName(_fromUtf8("standardImage"))
        self.horizontalLayout_3.addWidget(self.standardImage)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.outputTabs.addTab(self.standard, _fromUtf8(""))
        self.bootstrap = QtGui.QWidget()
        self.bootstrap.setObjectName(_fromUtf8("bootstrap"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.bootstrap)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.bootstrapImage = QtGui.QLabel(self.bootstrap)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bootstrapImage.sizePolicy().hasHeightForWidth())
        self.bootstrapImage.setSizePolicy(sizePolicy)
        self.bootstrapImage.setText(_fromUtf8(""))
        self.bootstrapImage.setObjectName(_fromUtf8("bootstrapImage"))
        self.horizontalLayout_2.addWidget(self.bootstrapImage)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.outputTabs.addTab(self.bootstrap, _fromUtf8(""))
        self.summary = QtGui.QWidget()
        self.summary.setObjectName(_fromUtf8("summary"))
        self.gridLayout_3 = QtGui.QGridLayout(self.summary)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.summary)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.outputTabs.addTab(self.summary, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.outputTabs, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.outputPage)
        self.inputMainHorizontalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addLayout(self.inputMainHorizontalLayout, 0, 0, 1, 1)
        PhylogeneticVisualization.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PhylogeneticVisualization)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuExport = QtGui.QMenu(self.menuFile)
        self.menuExport.setObjectName(_fromUtf8("menuExport"))
        self.menuMode = QtGui.QMenu(self.menubar)
        self.menuMode.setObjectName(_fromUtf8("menuMode"))
        PhylogeneticVisualization.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(PhylogeneticVisualization)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionRax = QtGui.QAction(PhylogeneticVisualization)
        self.actionRax.setCheckable(True)
        self.actionRax.setChecked(True)
        self.actionRax.setObjectName(_fromUtf8("actionRax"))
        self.actionNotRaxA = QtGui.QAction(PhylogeneticVisualization)
        self.actionNotRaxA.setCheckable(True)
        self.actionNotRaxA.setObjectName(_fromUtf8("actionNotRaxA"))
        self.actionNotRaxB = QtGui.QAction(PhylogeneticVisualization)
        self.actionNotRaxB.setCheckable(True)
        self.actionNotRaxB.setObjectName(_fromUtf8("actionNotRaxB"))
        self.actionNotRaxC = QtGui.QAction(PhylogeneticVisualization)
        self.actionNotRaxC.setCheckable(True)
        self.actionNotRaxC.setObjectName(_fromUtf8("actionNotRaxC"))
        self.actionStandardJPG = QtGui.QAction(PhylogeneticVisualization)
        self.actionStandardJPG.setObjectName(_fromUtf8("actionStandardJPG"))
        self.actionBootstrapJPG = QtGui.QAction(PhylogeneticVisualization)
        self.actionBootstrapJPG.setObjectName(_fromUtf8("actionBootstrapJPG"))
        self.actionTextFile = QtGui.QAction(PhylogeneticVisualization)
        self.actionTextFile.setObjectName(_fromUtf8("actionTextFile"))
        self.actionWindowsDirectory = QtGui.QAction(PhylogeneticVisualization)
        self.actionWindowsDirectory.setObjectName(_fromUtf8("actionWindowsDirectory"))
        self.actionRAXDirectory = QtGui.QAction(PhylogeneticVisualization)
        self.actionRAXDirectory.setObjectName(_fromUtf8("actionRAXDirectory"))
        self.actionTreesDirectory = QtGui.QAction(PhylogeneticVisualization)
        self.actionTreesDirectory.setObjectName(_fromUtf8("actionTreesDirectory"))
        self.menuExport.addAction(self.actionStandardJPG)
        self.menuExport.addAction(self.actionBootstrapJPG)
        self.menuExport.addAction(self.actionTextFile)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.actionWindowsDirectory)
        self.menuExport.addAction(self.actionRAXDirectory)
        self.menuExport.addAction(self.actionTreesDirectory)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuMode.addAction(self.actionRax)
        self.menuMode.addAction(self.actionNotRaxA)
        self.menuMode.addAction(self.actionNotRaxB)
        self.menuMode.addAction(self.actionNotRaxC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(PhylogeneticVisualization)
        self.stackedWidget.setCurrentIndex(0)
        self.outputTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PhylogeneticVisualization)

    def retranslateUi(self, PhylogeneticVisualization):
        PhylogeneticVisualization.setWindowTitle(_translate("PhylogeneticVisualization", "Phylogenetic Visualization", None))
        self.inputFileBtn.setText(_translate("PhylogeneticVisualization", "Select Input File", None))
        self.windowSizeLabel.setText(_translate("PhylogeneticVisualization", "Window Size:", None))
        self.windowOffsetLabel.setText(_translate("PhylogeneticVisualization", "Window Offset:", None))
        self.runBtn.setText(_translate("PhylogeneticVisualization", "Run", None))
        self.label.setText(_translate("PhylogeneticVisualization", "notRaxA", None))
        self.label_2.setText(_translate("PhylogeneticVisualization", "notRaxB", None))
        self.label_3.setText(_translate("PhylogeneticVisualization", "notRaxC", None))
        self.outputTabs.setTabText(self.outputTabs.indexOf(self.standard), _translate("PhylogeneticVisualization", "Standard", None))
        self.outputTabs.setTabText(self.outputTabs.indexOf(self.bootstrap), _translate("PhylogeneticVisualization", "Boostrap", None))
        self.pushButton_2.setText(_translate("PhylogeneticVisualization", "PushButton", None))
        self.outputTabs.setTabText(self.outputTabs.indexOf(self.summary), _translate("PhylogeneticVisualization", "Summary", None))
        self.menuFile.setTitle(_translate("PhylogeneticVisualization", "File", None))
        self.menuExport.setTitle(_translate("PhylogeneticVisualization", "Export...", None))
        self.menuMode.setTitle(_translate("PhylogeneticVisualization", "Mode", None))
        self.actionOpen.setText(_translate("PhylogeneticVisualization", "Open...", None))
        self.actionOpen.setShortcut(_translate("PhylogeneticVisualization", "Ctrl+O", None))
        self.actionRax.setText(_translate("PhylogeneticVisualization", "Rax", None))
        self.actionNotRaxA.setText(_translate("PhylogeneticVisualization", "Not Rax A", None))
        self.actionNotRaxB.setText(_translate("PhylogeneticVisualization", "Not Rax B", None))
        self.actionNotRaxC.setText(_translate("PhylogeneticVisualization", "Not Rax C", None))
        self.actionStandardJPG.setText(_translate("PhylogeneticVisualization", "Standard JPG", None))
        self.actionBootstrapJPG.setText(_translate("PhylogeneticVisualization", "Bootstrap JPG ", None))
        self.actionTextFile.setText(_translate("PhylogeneticVisualization", "Text File", None))
        self.actionWindowsDirectory.setText(_translate("PhylogeneticVisualization", "Windows Directory", None))
        self.actionRAXDirectory.setText(_translate("PhylogeneticVisualization", "RAX Directory", None))
        self.actionTreesDirectory.setText(_translate("PhylogeneticVisualization", "Trees Directory", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PhylogeneticVisualization = QtGui.QMainWindow()
    ui = Ui_PhylogeneticVisualization()
    ui.setupUi(PhylogeneticVisualization)
    PhylogeneticVisualization.show()
    sys.exit(app.exec_())

