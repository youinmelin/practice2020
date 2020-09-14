from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui
import sys
import _thread
import time
import conversion

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img/bg.png')))
        self.centralwidget.setPalette(palette)
        input_img = QtGui.QPixmap('img/input_test.png')
        self.input_img.setPixmap(input_img)

        export_img = QtGui.QPixmap('img/output_test.png')
        self.export_img.setPixmap(export_img)


    def openfile(self):
        # 打开选择文件的对话框
        openfile_name = QFileDialog.getOpenFileName()
        if openfile_name [0] != '':
            self.input_path = openfile_name[0]
            self.show_input_img(self.input_path)


    def show_input_img(self, file_path):
        print(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    main.pushButton_input.clicked.connect(main.openfile)
    # main.pushButton_conversion.clicked.connect(main.start_conversion)
    sys.exit(app.exec_())