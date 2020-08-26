# encoding = utf-8
__author__ = "Albert"

import xlrd
import xlsxwriter


# 读取excel
def excel():

    workbook = xlrd.open_workbook("C:\\Users\\Albert\\Desktop\\WPS\\天生无极球衣信息.xlsx")
    sheet = workbook.sheet_by_name("Sheet1")
    dat = []
    for i in range(1, 5):
        for a in range(sheet.nrows):
            cells = sheet.row_values(a)
            data = str(cells[i])
            dat.append(data)
    return dat


b = excel()
print(b)

workbook1 = xlsxwriter.Workbook("球衣信息表.xlsx")
worksheet = workbook1.add_worksheet("信息表")
worksheet.write_column("A1", b[3:12])
worksheet.write_column("B1", b[15:24])
worksheet.write_column("C1", b[27:36])
worksheet.write_column("D1", b[39:48])
workbook1.close()


# def test(s):
#     for c in s:
#         if c is not None:
#             print(c)
#
#
# print(test(b))
