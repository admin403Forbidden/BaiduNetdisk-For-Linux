# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.left_close = QtWidgets.QPushButton(self.centralwidget)
        self.left_close.setGeometry(QtCore.QRect(20, 20, 21, 21))
        self.left_close.setText("")
        self.left_close.setObjectName("left_close")
        self.left_visit = QtWidgets.QPushButton(self.centralwidget)
        self.left_visit.setGeometry(QtCore.QRect(50, 20, 21, 21))
        self.left_visit.setText("")
        self.left_visit.setObjectName("left_visit")
        self.left_mini = QtWidgets.QPushButton(self.centralwidget)
        self.left_mini.setGeometry(QtCore.QRect(80, 20, 21, 21))
        self.left_mini.setText("")
        self.left_mini.setObjectName("left_mini")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 941, 41))
        self.label.setObjectName("label")
        self.labelN = QtWidgets.QLabel(self.centralwidget)
        self.labelN.setGeometry(QtCore.QRect(220, 600, 941, 41))
        self.labelN.setObjectName("labelN")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 151, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 100, 891, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 50, 71, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 50, 71, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 50, 71, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 50, 71, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.left_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_widget.setGeometry(QtCore.QRect(0, 0, 181, 691))
        self.left_widget.setObjectName("left_widget")
        self.right_widget = QtWidgets.QWidget(self.centralwidget)
        self.right_widget.setGeometry(QtCore.QRect(179, -1, 941, 691))
        self.right_widget.setObjectName("right_widget")
        self.right_widget.raise_()
        self.left_widget.raise_()
        self.label.raise_()
        self.left_close.raise_()
        self.left_visit.raise_()
        self.left_mini.raise_()
        self.label_2.raise_()
        self.labelN.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelN.setText(_translate("MainWindow",
                                      """<html><head/><body><span style=\" font-size:13pt;\">当前地址：/apps/bypy</span></p></body></html>"""))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">百度网盘 BaiduNetDisk For Centos</span></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "添加时间"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "bypy"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "创建时自动添加"))
        ##########
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.pushButton_2.setText(_translate("MainWindow", "上传"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_4.setText(_translate("MainWindow", "重命名"))
        self.centralwidget.setStyleSheet('''
        QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
                }
                    QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')
        self.right_widget.setStyleSheet('''
        QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
        }
        QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        ''')
        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        MainWindow.setWindowOpacity(0.98) # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

