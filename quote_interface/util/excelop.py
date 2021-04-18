import xlrd


class ExcelOp:

    def __init__(self,path,sheet_name):
        self.path=path
        self.sheet_name=sheet_name
        self.workbook=xlrd.open_workbook(path)
        self.sheet=self.workbook.sheet_by_name(sheet_name)

    def get_row(self):
        rows=self.sheet.nrows
        return rows

    def get_col(self):
        cols=self.sheet.ncols
        return cols

    def get_value(self,row,col):
        value=self.sheet.cell_value(row,col)
        return value

# e=ExcelOp('C:\\Users\\pc\\PycharmProjects\\project01\\autotest\\quote_interface\\config\\用例.xlsx','adduseryongli')
# print(e.get_row())
# print(e.get_col())
# print(e.get_value(1,2))