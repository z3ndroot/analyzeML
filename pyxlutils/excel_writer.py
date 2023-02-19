from openpyxl import Workbook

class ExcelWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        wb = Workbook()
        sheet = wb.active

        sheet.cell(row=1, column=1, value="Message")
        sheet.cell(row=1, column=2, value="Result")

        for row_idx, row_data in enumerate(data, start=2):
            sheet.cell(row=row_idx, column=1, value=row_data[0])
            sheet.cell(row=row_idx, column=2, value=row_data[1])

        wb.save(self.filename)