import os

from window import Ui_Dialog
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication  # 导入qt窗体类
from PyQt5.QtWidgets import QFileDialog
from utils.sort_excel_by_key_argv import sort_file
# from utils.panda_01_write_excel import write
# import yaml_read


class Main(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


    def sort_file(self):
        # open "open file" window
        filename = QFileDialog.getOpenFileName()
        print("open_file")
        if filename[0] != '':
            self.input_path = filename[0]
            print(self.input_path)
            self.new_filename, self.message = sort_file(self.input_path)
            self.show_result('%s' %self.message)
            # 如果成功筛选，该按钮变为可以点击
            if self.new_filename != '':
                self.toolButton_2.setDisabled(False)
            else:
                self.toolButton_2.setDisabled(True)



    def show_result(self, result_str):
        self.user_textBrowser.setText(result_str)

    def open_file(self):
        os.startfile(self.new_filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    main.toolButton.clicked.connect(main.sort_file)
    main.toolButton_2.clicked.connect(main.open_file)
    sys.exit(app.exec_())

