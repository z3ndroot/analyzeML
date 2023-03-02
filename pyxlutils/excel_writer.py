from openpyxl import Workbook


class ExcelWriter:
    def __init__(self, filename, name_column):
        self.filename = filename
        self._name_column = name_column

    def write_data(self, data):
        wb = Workbook()
        sheet = wb.active

        sheet.append(self._name_column)
        for row_data in data:
            sheet.append(row_data)

        wb.save(self.filename)
