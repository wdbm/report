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
version = "2015-08-09T2226Z"

import sys
import os
from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import *

class Report(QtGui.QMainWindow):

    def __init__(self):
        super(Report, self).__init__()
        # set view
        self.status_view = "window"
        # set colours
        self.status_colours = "light"
        # set font size
        self.font_size = 22
        # font database
        self.font_database = QtGui.QFontDatabase()
        # add font cmtex9
        self.font_file_cmtex9="cmtex9.ttf"
        self.font_identifier_cmtex9 = QFontDatabase.addApplicationFont(
            self.font_file_cmtex9
        )
        self.fontFamilyName_cmtex9 = self.font_database.applicationFontFamilies(
            self.font_identifier_cmtex9
        )[0]
        self.update_font()

        self.initialise_UI()

    def update_font(self):
        # add font cmtex9
        self.font_cmtex9 = QFont(self.fontFamilyName_cmtex9, self.font_size)
        # add font Courier Prime
        self.font_CourierPrime = QFont("Courier Prime", self.font_size)
        # set default font
        self.font_current = self.font_cmtex9
        self.font_current.setFixedPitch(True)
        self.setFont(self.font_current)

    def initialise_UI(self):
        action_toggle_view = QtGui.QAction("toggle view", self)
        action_toggle_view.setShortcut("Ctrl+F")
        action_toggle_view.setStatusTip("toggle fullscreen/window view")
        action_toggle_view.triggered.connect(self.toggle_view)

        action_toggle_colours = QtGui.QAction("toggle colours", self)
        action_toggle_colours.setShortcut("Ctrl+D")
        action_toggle_colours.setStatusTip("toggle light/dark colours")
        action_toggle_colours.triggered.connect(self.toggle_colours)

        action_set_font_size = QtGui.QAction("set font size", self)
        action_set_font_size.setShortcut("Ctrl+T")
        action_set_font_size.setStatusTip("set font size")
        action_set_font_size.triggered.connect(self.set_font_size)

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

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&file")
        file_menu.addAction(action_toggle_view)
        file_menu.addAction(action_toggle_colours)
        file_menu.addAction(action_set_font_size)
        file_menu.addAction(action_new)
        file_menu.addAction(action_save)
        file_menu.addAction(action_open)
        file_menu.addAction(action_close)

        self.text = QtGui.QTextEdit(self)
        self.text.setStyleSheet(
            "QTextEdit{color: #000000; background-color: #ffffff;}"
        )

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

    def toggle_colours(self):
        if self.status_colours == "light":
            self.text.setStyleSheet(
                "QTextEdit{color: #ffffff; background-color: #000000;}"
            )
            self.status_colours == "dark"
            return
        if self.status_colours == "dark":
            self.text.setStyleSheet(
                "QTextEdit{color: #000000; background-color: #ffffff;}"
            )
            self.status_colours == "light"
            return

    def set_font_size(self):
        font_size, ok = QtGui.QInputDialog.getText(
            self,
            "font size", 
            "enter font size:"
        )
        if ok:
            self.font_size = int(font_size)
            self.update_font()

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
