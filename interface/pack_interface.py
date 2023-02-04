from PySide2 import QtWidgets

from .interface_settings import  Ui_MainWindow


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_xlsx)
        self.pushButton_2.clicked.connect(self.open_rules)
        self.pushButton_3.clicked.connect(self.path_to_file)

    def open_xlsx(self):
        xlsx_file = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.xlsx")
        self.lineEdit.setText(xlsx_file[0])

    def open_rules(self):
        rules_file = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.txt")
        self.lineEdit_2.setText(rules_file[0])

    def path_to_file(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.lineEdit_3.setText(path+"/result.xlsx")


