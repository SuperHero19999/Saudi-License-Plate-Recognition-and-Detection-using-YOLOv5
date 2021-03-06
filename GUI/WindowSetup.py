# Form implementation generated from reading ui file 'GUI/FrontPage.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QPixmap, QImage
import mysql.connector
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class Ui_LicensePlateProject(object):
    def __init__(self):
        self.ShouldStartDetection = False

    def setupUi(self, LicensePlateProject):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        LicensePlateProject.setObjectName("LicensePlateProject")
        LicensePlateProject.resize(1040, 781)
        LicensePlateProject.setFixedSize(1040, 781)
        LicensePlateProject.setFont(font)
        LicensePlateProject.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        LicensePlateProject.setStyleSheet('background-image: url(GUI/Photos/Background.jpg);')
        LicensePlateProject.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        LicensePlateProject.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

        self.centralwidget = QtWidgets.QWidget(LicensePlateProject)
        self.centralwidget.setObjectName("centralwidget")

        self.Frame = QtWidgets.QLabel(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(10, 10, 600, 460))
        self.Frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Frame.setStyleSheet("border:2px solid black;\n" "padding: 10px;\n" "border-radius: 25px;")
        self.Frame.setMidLineWidth(0)
        self.Frame.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Frame.setObjectName("Frame")

        self.StartDetection = QtWidgets.QPushButton(self.centralwidget)
        self.StartDetection.setGeometry(QtCore.QRect(20, 490, 241, 51))
        self.StartDetection.setStyleSheet(
            "background: #ffb09e;\n" "color:#000000;\n" "border:2px solid #232526;\n" "border-radius:25px;\n" "hover:{\n" "background: #0aff1e;\n" "}")
        self.StartDetection.setObjectName("StartDetection")
        self.StartDetection.clicked.connect(self.OnButtonPressed_DetectActivation)

        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(340, 490, 241, 51))
        self.Exit.setStyleSheet(
            "background: #ffb09e;\n" "color:#000000;\n" "border:2px solid #232526;\n" "border-radius:25px;")
        self.Exit.setObjectName("Exit")
        self.Exit.clicked.connect(self.OnButtonPressed_ExitProgram)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        self.LicensePlateImage = QtWidgets.QLabel(self.centralwidget)
        self.LicensePlateImage.setGeometry(QtCore.QRect(80, 560, 441, 171))
        self.LicensePlateImage.setFont(font)
        self.LicensePlateImage.setStyleSheet("")
        self.LicensePlateImage.setText("")
        self.LicensePlateImage.setPixmap(QtGui.QPixmap('GUI/Photos/Sc1.png'))
        self.LicensePlateImage.setScaledContents(True)
        self.LicensePlateImage.setObjectName("LicensePlateImage")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.ArabicNumb = QtWidgets.QLabel(self.centralwidget)
        self.ArabicNumb.setGeometry(QtCore.QRect(90, 570, 221, 71))
        self.ArabicNumb.setStyleSheet(
            "content-justify:center;\n" "background: #e3e2e8;\n" "color:#000000;\n" "font: 25pt;")
        self.ArabicNumb.setText("")
        self.ArabicNumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ArabicNumb.setObjectName("ArabicNumb")

        self.EnglishNumb = QtWidgets.QLabel(self.centralwidget)
        self.EnglishNumb.setGeometry(QtCore.QRect(90, 650, 221, 71))
        self.EnglishNumb.setFont(font)
        self.EnglishNumb.setStyleSheet(
            "content-justify:center;\n" "background: #e3e2e8;\n" "color:#000000;\n" "font: 25pt;")
        self.EnglishNumb.setText("")
        self.EnglishNumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnglishNumb.setObjectName("EnglishNumb")

        self.ArabicLetter = QtWidgets.QLabel(self.centralwidget)
        self.ArabicLetter.setGeometry(QtCore.QRect(320, 570, 151, 71))
        self.ArabicLetter.setStyleSheet(
            "content-justify:center;\n" "background: #e3e2e8;\n" "color:#000000;\n" "font: 25pt;")
        self.ArabicLetter.setText("")
        self.ArabicLetter.setScaledContents(False)
        self.ArabicLetter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ArabicLetter.setObjectName("ArabicLetter")

        self.EnglishLetter = QtWidgets.QLabel(self.centralwidget)
        self.EnglishLetter.setGeometry(QtCore.QRect(320, 650, 151, 71))
        self.EnglishLetter.setStyleSheet(
            "content-justify:center;\n" "background: #e3e2e8;\n" "color:#000000;\n" "font: 25pt;")
        self.EnglishLetter.setText("")
        self.EnglishLetter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnglishLetter.setObjectName("EnglishLetter")

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum,
                                                QtWidgets.QSizePolicy.Policy.Maximum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(671, 11, 351, 721))
        self.tableWidget.setSizePolicy(self.sizePolicy)
        self.tableWidget.setStyleSheet(
            "background-color:rgb(179, 235, 255);\n" "border-radius: 25px;\n" "padding: 20px;\n" "background: #ffffff;\n" "color:#000000;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(25)
        self.tableWidget.setMidLineWidth(25)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(82)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        item = QtWidgets.QTableWidgetItem()
        item.setText('License plate')
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('ID')
        self.tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Name')
        self.tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Phone')
        self.tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Car type')
        self.tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Color')
        self.tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Gender')
        self.tableWidget.setItem(6, 0, item)

        self.sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())

        self.StartDetection.raise_()
        self.Exit.raise_()
        self.LicensePlateImage.raise_()
        self.EnglishNumb.raise_()
        self.ArabicNumb.raise_()
        self.Frame.raise_()
        self.ArabicLetter.raise_()
        self.EnglishLetter.raise_()
        self.tableWidget.raise_()
        LicensePlateProject.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LicensePlateProject)
        self.statusbar.setObjectName("statusbar")
        LicensePlateProject.setStatusBar(self.statusbar)
        self.topMenu = QtWidgets.QMenuBar(LicensePlateProject)
        self.topMenu.setGeometry(QtCore.QRect(0, 0, 1040, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy)
        self.topMenu.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.topMenu.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.topMenu.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.topMenu.setAutoFillBackground(False)
        self.topMenu.setDefaultUp(False)
        self.topMenu.setNativeMenuBar(True)
        self.topMenu.setObjectName("topMenu")
        self.menuDetection_and_Recognition = QtWidgets.QMenu(self.topMenu)
        self.menuDetection_and_Recognition.setObjectName("menuDetection_and_Recognition")
        LicensePlateProject.setMenuBar(self.topMenu)
        self.topMenu.addAction(self.menuDetection_and_Recognition.menuAction())

        self.retranslateUi(LicensePlateProject)
        QtCore.QMetaObject.connectSlotsByName(LicensePlateProject)

    def retranslateUi(self, LicensePlateProject):
        _translate = QtCore.QCoreApplication.translate
        LicensePlateProject.setWindowTitle(_translate("LicensePlateProject", "License Plate Detection and Recognition"))
        self.Frame.setText(_translate("LicensePlateProject", "Frame"))
        self.StartDetection.setText(_translate("LicensePlateProject", "Start Detection"))
        self.Exit.setText(_translate("LicensePlateProject", "Exit"))
        self.tableWidget.setSortingEnabled(False)
        self.menuDetection_and_Recognition.setTitle(_translate("LicensePlateProject", "Detection and Recognition"))

    def ShowResults(self, En_Letters, En_Numbers, Ar_Letters, Ar_Numbers):
        try:
            DB = mysql.connector.connect(
                host="sql11.freesqldatabase.com",
                user="sql11492437",
                password="xNzexJNVuX",
                database="sql11492437",
                port="3307"
            )
            SQL_Cursor = DB.cursor()

            Search = En_Numbers + En_Letters
            SQL_Cursor.execute('SELECT * FROM information WHERE plate like "{}"'.format(Search))
            Info = SQL_Cursor.fetchall()

            for Row, Col in enumerate(Info):
                for i, n in enumerate(Col):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(n))
                    self.tableWidget.setItem(i, 1, item)

            for Row, Col in enumerate(Info):
                for i, n in enumerate(Col):
                    if Search == n:
                        self.EnglishLetter.setText(En_Letters)
                        self.EnglishNumb.setText(En_Numbers)
                        self.ArabicLetter.setText(Ar_Letters)
                        self.ArabicNumb.setText(Ar_Numbers)
                        break

        except mysql.connector.Error as Error:
            self.DisplayMessage(str(Error))

    def OnButtonPressed_ExitProgram(self):
        quit()

    def OnButtonPressed_DetectActivation(self):
        if self.ShouldStartDetection is False:
            self.StartDetection.setText("Stop Detection")
            self.Frame.setPixmap(QPixmap('Out/Frame.png'))
            self.ShouldStartDetection = True
        else:
            self.StartDetection.setText("Start Detection")
            self.Frame.setPixmap(QPixmap())
            self.ShouldStartDetection = False
