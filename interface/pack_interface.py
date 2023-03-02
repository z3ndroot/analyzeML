from PySide2 import QtWidgets

from .interface_settings import Ui_MainWindow
from pathcheck import check_path
from pyxlutils import (
    ExcelReader,
    ExcelWriter,
    analyze_messages_with_rules,
    analyze_meta_with_rules,
    check_predicate,
    JSONMetaData,

)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_xlsx)
        self.pushButton_2.clicked.connect(self.open_rules)
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

    def analyze(self):
        path_rules = self.lineEdit_2.text()

        if not check_path(path_rules):
            self.MessageBox_2.setWindowTitle("PathRules")
            self.MessageBox_2.setText("The rules file does not exist or the path is wrong")
            self.MessageBox_2.exec_()
            return

        error = check_predicate(path_rules)

        if error:
            self.MessageBox_2.setWindowTitle("PredicateError")
            self.MessageBox_2.setText(error)
            self.MessageBox_2.exec_()
            return

        if not self.__file:
            self.MessageBox_2.setWindowTitle("FileOpen")
            self.MessageBox_2.setText("The message file is not selected or the path is wrong")
            self.MessageBox_2.exec_()
            return

        path_save, _ = QtWidgets.QFileDialog.getSaveFileName(self, filter="*.xlsx")

        if not path_save:
            self.MessageBox_2.setWindowTitle("SaveFile")
            self.MessageBox_2.setText("File to save is not selected")
            self.MessageBox_2.exec_()
            return

        if isinstance(self.__file, ExcelReader):
            messages = self.__file.get_messages(
                sheet_name=self.comboBox.currentText(),
                column_name=self.comboBox_2.currentText()
            )
            data = analyze_messages_with_rules(messages, path_rules)

            ew = ExcelWriter(path_save, name_column=["Message", "Result"])
            ew.write_data(data)

        elif isinstance(self.__file, JSONMetaData):
            data = analyze_meta_with_rules(self.__file.meta_info, path_rules)

            ew = ExcelWriter(path_save, name_column=["Id", "Message", "Result"])
            ew.write_data(data)
        self.MessageBox.setText(f"{path_save} file saved✅")
        self.MessageBox.exec_()
