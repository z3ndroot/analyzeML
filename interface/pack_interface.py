from PySide2 import QtWidgets

from .interface_settings import Ui_MainWindow
from pathcheck import check_path
from pyxlutils import (
    ExcelReader,
    ExcelWriter,
    analyze_messages_with_rules,
    JSONMetaData,
)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_xlsx)
        self.pushButton_2.clicked.connect(self.open_rules)
        self.pushButton_3.clicked.connect(self.path_to_file)
        self.comboBox.currentTextChanged.connect(self.update_columns)
        self.pushButton_4.clicked.connect(self.analyze)
        self.__file = None

    def open_xlsx(self):
        self.comboBox.clear()
        path, extension = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.xlsx;;*.json")
        self.lineEdit.setText(path)
        file = self.lineEdit.text()

        if not check_path(file):
            return
        if extension == "*.xlsx":
            self.__file = ExcelReader(file)
            self.comboBox.addItems(self.__file.sheet_names)
        elif extension == "*.json":
            self.__file = JSONMetaData(file)
            self.comboBox_2.clear()


    def update_columns(self):
        if self.comboBox.currentText():
            self.comboBox_2.clear()
            name_columns = self.__file.columns_names(self.comboBox.currentText())
            self.comboBox_2.addItems(name_columns)

    def open_rules(self):
        rules_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.txt")
        self.lineEdit_2.setText(rules_file)

    def path_to_file(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.lineEdit_3.setText(path)

    def analyze(self):
        path_save = self.lineEdit_3.text()
        path_rules = self.lineEdit_2.text()

        if not (check_path(path_rules) and check_path(path_save)):
            return
        if isinstance(self.__file, ExcelReader):
            messages = self.__file.get_messages(
                sheet_name=self.comboBox.currentText(),
                column_name=self.comboBox_2.currentText()
            )
            result = analyze_messages_with_rules(messages, path_rules)

        elif isinstance(self.__file, JSONMetaData):
            # TODO...
            pass


        ew = ExcelWriter(path_save+"/result.xlsx")
        ew.write_data(result)
        self.MessageBox.exec_()
