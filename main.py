# -*- coding:utf-8 -*-
# author:
from bypy import ByPy
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from upload import *
import sys

class UL(QtWidgets.QMainWindow,UpLoad):
    def __init__(self):
        super(UL,self).__init__()
        self.setupUi(self)
        self.registerEvent()
    def registerEvent(self):
        pass


class MainUI(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.registerEvent()

    def registerEvent(self):
        _translate = QtCore.QCoreApplication.translate
        self.left_close.clicked.connect(self.Exit)
        self.left_mini.clicked.connect(self.Mini)
        item_1 = self.tableWidget.item(0, 0)
        item_1.setText(_translate("MainWindow", ".."))
        item_1 = self.tableWidget.item(0, 1)
        item_1.setText(_translate("MainWindow", "BACK"))
        item_1 = self.tableWidget.item(0, 2)
        item_1.setText(_translate("MainWindow", "返回"))
        self.pushButton_2.clicked.connect(self.on_btn_click)
        Folder = QtGui.QIcon()
        Folder.addPixmap(QtGui.QPixmap("Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for i in range(1,10):

            self.tableWidget.setRowCount(i+1)
            newItem = QTableWidgetItem()
            newItem.setIcon(Folder)
            self.tableWidget.setItem(i, 0,newItem)
            # 添加数据
            newItem = QTableWidgetItem('张三')
            self.tableWidget.setItem(i, 0, newItem)

            newItem = QTableWidgetItem('男')
            self.tableWidget.setItem(i, 1, newItem)

            newItem = QTableWidgetItem('160')
            self.tableWidget.setItem(i, 2, newItem)
    def on_btn_click(self):
        self.up = UL()
        self.up.show()
    def Exit(self):
        self.close()
    def Mini(self):
        self.showMinimized()

# 获取一个bypy对象，封装了所有百度云文件操作的方法
bp = ByPy()
print(bp.list(""))
'''
# 百度网盘创建文件夹zhoulong
bp.mkdir(remotepath = 'Jizy')
#上传文件至文件夹
# upload中参数代表复制文件，默认值为'overwrite'，指定'newcopy'不会覆盖重复文件
bp.upload(localpath= r'上传文件绝对路径', remotepath= 'zhoulong', ondup='newcopy')
print('上传完成！！')
bp.download(remotepath = 'zhoulong', localpath = r'下载文件输出文件夹')
print('下载完成！！')

print("ST")
bp.download(remotepath="骆驼祥子   读书笔记 7.pptx",localpath=r"F:\\Baidu\\")
print("Done")'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())
