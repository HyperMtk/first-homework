# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from ocrUi import Ui_MainWindow
from ocr import *
import sys, os, shutil

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('OCR图像文字识别')

    #选择图像文件打开
    def openFile(self):
        fileName = str(QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '/', '图像文件(*.bmp; *.jpg; *.jpeg; *.png)')[0])
        if fileName == '':
            return
        self.showFileName.setText(fileName)
        with open('temp', 'w') as f:
            f.write(fileName)

    #输出为文本文件
    def output(self):
        outputFileName, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', '/', "文本文件(*.txt)")

        if not ok:
            return
        if os.path.exists('temp2'):
            shutil.copyfile('temp2', outputFileName)
            QtWidgets.QMessageBox.information(self, '保存文件', '保存文件成功', QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.warning(self, '警告', '保存文件失败')

    #获取识别结果
    def useOcr(self):
        try:
            with open('temp', 'r') as f:
                fileName = f.read()
        except IOError:
            QtWidgets.QMessageBox.warning(self, '警告', '打开文件失败')
            return

        result = getResult(fileName)
        with open('temp2', 'w+') as f:
            for i in result:
                f.write(i['words'])
            f.seek(0, 0)
            self.showResult.setText(f.read())

    #关闭程序时删除临时文件
    def closeEvent(self, event):
        if os.path.exists('temp'):
            os.remove('temp')
        if os.path.exists('temp2'):
            os.remove('temp2')
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
