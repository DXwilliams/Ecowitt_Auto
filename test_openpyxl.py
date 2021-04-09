from pprint import pprint
import openpyxl
import pytest

def read_excel(file,sheet_name):
    """读取excel 当中的数据"""
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    rows = list(sheet.rows)
    #列表推导式，map函数
    data = []
    for row in rows[1:]:
        row_data = []
        for cell in row:
            row_data.append(cell.value)
        data.append(row_data)
    return data

if __name__ == '__main__':
    pass
    # a = read_excel("api_practice.xlsx","demo")
    # pprint(a)