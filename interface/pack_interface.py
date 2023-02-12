from PySide2 import QtWidgets

from .interface_settings import  Ui_MainWindow
from analysis_functions import FileXSLX

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_xlsx)
        self.pushButton_2.clicked.connect(self.open_rules)
        self.pushButton_3.clicked.connect(self.path_to_file)
        self.comboBox.currentTextChanged.connect(self.get_name_columns)
        self.__file = None


    def open_xlsx(self):
        self.comboBox.clear()
        xlsx_file = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.xlsx")
        self.lineEdit.setText(xlsx_file[0])
        if self.lineEdit.text():
            self.__file = FileXSLX(self.lineEdit.text())
            self.comboBox.addItems(self.__file.sheet_names)

    def get_name_columns(self):
        if self.comboBox.currentText():
            self.comboBox_2.clear()
            name_columns = self.__file.columns_names(self.comboBox.currentText())
            self.comboBox_2.addItems(name_columns)


    def open_rules(self):
        rules_file = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.txt")
        self.lineEdit_2.setText(rules_file[0])

    def path_to_file(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.lineEdit_3.setText(path+"/result.xlsx")


