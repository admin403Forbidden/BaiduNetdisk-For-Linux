# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UpLoad(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 230, 431, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 71, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 230, 51, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 290, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 71, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 301, 431, 21))
        self.label_3.setObjectName("label_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(90, 50, 461, 171))
        self.listView.setObjectName("listView")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 601, 20))
        self.label_4.setObjectName("label_4")
        self.left_close = QtWidgets.QPushButton(self.centralwidget)
        self.left_close.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.left_close.setText("")
        self.left_close.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 621, 341))
        self.widget.setObjectName("widget")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.widget.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.listView.raise_()
        self.label_4.raise_()
        self.left_close.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "上传"))
        self.label.setText(_translate("MainWindow", "本地地址："))
        self.pushButton_2.setText(_translate("MainWindow", "上传"))
        self.label_2.setText(_translate("MainWindow", "网盘地址："))
        self.label_3.setText(_translate("MainWindow", "apps\\bypy\\"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">上传文件</p></body></html>"))
        self.centralwidget.setStyleSheet('''
           QWidget#widget{
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
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        MainWindow.setWindowOpacity(0.98) # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UpLoad()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
