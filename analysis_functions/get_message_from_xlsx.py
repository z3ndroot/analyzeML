from openpyxl import load_workbook


class FileXSLX:
    def __init__(self, filename):
        self.wb = load_workbook(filename=filename)
        self.names_columns_dict = None

    @property
    def sheets_names(self):
        return self.wb.sheetnames

    def columns_names(self, name_sheet):
        worksheet = self.wb[name_sheet]
        iter_cols = worksheet.iter_cols(
            max_row=1,
            max_col=worksheet.max_column,
            values_only=True
        )
        columns_names = [title[0] for title in iter_cols]

        self.names_columns_dict = {title: num for num, title in enumerate(
            columns_names,
            start=1,
        ) if title is not None}

        return columns_names

    # TODO...
