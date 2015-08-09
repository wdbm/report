#! /usr/bin/python

################################################################################
#                                                                              #
# report                                                                       #
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

name    = "report"
version = "2015-08-09T2053Z"

import sys
import os
from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import *

class Report(QtGui.QMainWindow):

    def __init__(self):
        super(Report, self).__init__()
        # font database
        font_database = QtGui.QFontDatabase()
        # add font cmtex9
        font_file_cmtex9="cmtex9.ttf"
        font_identifier_cmtex9 = QFontDatabase.addApplicationFont(
            font_file_cmtex9
        )
        fontFamilyName_cmtex9 = font_database.applicationFontFamilies(
            font_identifier_cmtex9
        )[0]
        font_cmtex9 = QFont(fontFamilyName_cmtex9, 12)
        # add font Courier Prime
        font_CourierPrime = QFont("Courier Prime", 12)
        # set default font
        font_current = font_cmtex9
        font_current.setFixedPitch(True)
        self.setFont(font_current)
        # set view
        self.status_view = "window"
        self.initialise_UI()

    def initialise_UI(self):
        action_new = QtGui.QAction("new", self)
        action_new.setShortcut("Ctrl+N")
        action_new.setStatusTip("create new file")
        action_new.triggered.connect(self.new_file)

        action_save = QtGui.QAction("save", self)
        action_save.setShortcut("Ctrl+S")
        action_save.setStatusTip("save current file")
        action_save.triggered.connect(self.save_file)

        action_open = QtGui.QAction("open", self)
        action_open.setShortcut("Ctrl+O")
        action_open.setStatusTip("open a file")
        action_open.triggered.connect(self.openFile)

        action_close = QtGui.QAction("close", self)
        action_close.setShortcut("Ctrl+Q")
        action_close.setStatusTip("close report")
        action_close.triggered.connect(self.close)

        action_toggle_view = QtGui.QAction("toggle view", self)
        action_toggle_view.setShortcut("Ctrl+F")
        action_toggle_view.setStatusTip("toggle fullscreen/window view")
        action_toggle_view.triggered.connect(self.toggle_view)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&file")
        file_menu.addAction(action_toggle_view)
        file_menu.addAction(action_new)
        file_menu.addAction(action_save)
        file_menu.addAction(action_open)
        file_menu.addAction(action_close)

        self.text = QtGui.QTextEdit(self)

        self.setCentralWidget(self.text)
        self.setGeometry(300, 300, 300, 300)
        self.showMaximized()
        self.setWindowTitle("report")
        self.show()

    def toggle_view(self):
        if self.status_view == "window":
            self.showFullScreen()
            self.status_view = "fullscreen"
            return
        if self.status_view == "fullscreen":
            self.showMaximized()
            self.status_view = "window"
            return

    def new_file(self):
        self.text.clear()

    def save_file(self):
        filename = QtGui.QFileDialog.getsave_fileName(
            self,
            "save file",
            os.getenv("HOME")
        )
        file_1 = open(filename, "w")
        file_data = self.text.toPlainText()
        file_1.write(file_data)
        file_1.close()

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(
            self,
            "open file",
            os.getenv("HOME")
        )
        file_1 = open(filename, "r")
        file_data = file_1.read()
        self.text.setText(file_data)
        file_1.close()

def main():
    application = QtGui.QApplication(sys.argv)
    report = Report()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
