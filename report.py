#! /usr/bin/python

################################################################################
#                                                                              #
# report                                                                       #
#                                                                              #
# version: 2014-01-29T1803                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# The program report is a text editor.                                         #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

import sys
import os
#from PyQt4 import QtGui
from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import *

class Report(QtGui.QMainWindow):

    def __init__(self):
        super(Report, self).__init__()
        # font database
        fontDatabase = QtGui.QFontDatabase()
        # add font cmtex9
        fontFile_cmtex9="cmtex9.ttf"
        fontIdentifier_cmtex9 = QFontDatabase.addApplicationFont(fontFile_cmtex9)
        fontFamilyName_cmtex9 = fontDatabase.applicationFontFamilies(fontIdentifier_cmtex9)[0]
        font_cmtex9 = QFont(fontFamilyName_cmtex9, 12)
        # add font Courier Prime
        font_CourierPrime = QFont("Courier Prime", 12)
        # set default font
        font_current = font_cmtex9
        font_current.setFixedPitch(True)
        self.setFont(font_current)
        self.initUI()

    def initUI(self):
        newAction = QtGui.QAction('new', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('create new file')
        newAction.triggered.connect(self.newFile)

        saveAction = QtGui.QAction('save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('save current file')
        saveAction.triggered.connect(self.saveFile)

        openAction = QtGui.QAction('open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('open a file')
        openAction.triggered.connect(self.openFile)

        closeAction = QtGui.QAction('close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('close report')
        closeAction.triggered.connect(self.close)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&file')
        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(closeAction)

        self.text = QtGui.QTextEdit(self)

        self.setCentralWidget(self.text)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('report')
        self.show()

    def newFile(self):
        self.text.clear()

    def saveFile(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'save file', os.getenv('HOME'))
        file = open(fileName, 'w')
        fileData = self.text.toPlainText()
        file.write(fileData)
        file.close()

    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'open file', os.getenv('HOME'))
        file = open(fileName, 'r')
        fileData = file.read()
        self.text.setText(fileData)
        file.close()

def main():
    application = QtGui.QApplication(sys.argv)
    report = Report()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
