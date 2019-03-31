# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrUi.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.selectFileButton.setGeometry(QtCore.QRect(560, 170, 52, 21))
        self.selectFileButton.setObjectName("selectFileButton")
        self.ocrButton = QtWidgets.QPushButton(self.centralwidget)
        self.ocrButton.setGeometry(QtCore.QRect(150, 230, 112, 34))
        self.ocrButton.setObjectName("ocrButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(540, 230, 112, 34))
        self.exitButton.setObjectName("exitButton")
        self.outputButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(350, 230, 112, 34))
        self.outputButton.setObjectName("outputButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 130, 91, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 310, 81, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 40, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.showFileName = QtWidgets.QTextBrowser(self.centralwidget)
        self.showFileName.setGeometry(QtCore.QRect(180, 160, 371, 31))
        self.showFileName.setObjectName("showFileName")
        self.showResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.showResult.setGeometry(QtCore.QRect(150, 360, 531, 171))
        self.showResult.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        self.selectFileButton.clicked.connect(MainWindow.openFile)
        self.outputButton.clicked.connect(MainWindow.output)
        self.ocrButton.clicked.connect(MainWindow.useOcr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectFileButton.setText(_translate("MainWindow", "..."))
        self.ocrButton.setText(_translate("MainWindow", "识别"))
        self.exitButton.setText(_translate("MainWindow", "退出"))
        self.outputButton.setText(_translate("MainWindow", "输出为txt"))
        self.label.setText(_translate("MainWindow", "选择文件："))
        self.label_2.setText(_translate("MainWindow", "识别结果："))
        self.label_3.setText(_translate("MainWindow", " OCR图像文字识别"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


