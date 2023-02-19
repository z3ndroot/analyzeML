from PySide2 import QtWidgets

from .interface_settings import  Ui_MainWindow
from pyxlutils import (
    ExcelReader,
    ExcelWriter,
    analyze_messages_with_rules,
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
        xlsx_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, filter="*.xlsx")
        self.lineEdit.setText(xlsx_file)
        if self.lineEdit.text():
            self.__file = ExcelReader(self.lineEdit.text())
            self.comboBox.addItems(self.__file.sheet_names)

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
        self.lineEdit_3.setText(f"{path}/result.xlsx")

    def analyze(self):
        messages = self.__file.get_messages(
            sheet_name=self.comboBox.currentText(),
            column_name=self.comboBox_2.currentText()
        )
        result = analyze_messages_with_rules(messages, self.lineEdit_2.text())
        ew = ExcelWriter(self.lineEdit_3.text())
        ew.write_data(result)




