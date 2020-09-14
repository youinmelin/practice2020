from window import Ui_Dialog
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog  # 导入qt窗体类
from PyQt5.QtWidgets import QFileDialog


class Main(QMainWindow, Ui_Dialog):

    def open_file(self):
        filename = QFileDialog.getOpenFilename()
        if filename[0] != '':
            self.input_path = filename[0]
            print(self.input_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    main.toolButton.clicked(main.open_file)
    sys.exit(app.exec_())

