# encoding = utf-8
__author__ = "Albert"

import xlrd
import xlsxwriter


def get_rows():
    workbook = xlrd.open_workbook("C:\\Users\\Albert\\Desktop\\Nerve测试网节点奖励注册表.xlsx")
    sheet = workbook.sheet_by_name("Sheet3")
    # 获取列表行数、列数
    nrows = sheet.nrows
    cols = sheet.ncols
    print(cols)
    print(nrows)


# 读取excel
def excel():

    # workbook = xlrd.open_workbook("C:\\Users\\Albert\\Desktop\\WPS\\天生无极球衣信息.xlsx")
    # sheet = workbook.sheet_by_name("Sheet1")
    # dat = []
    # for i in range(1, 5):
    #     for a in range(sheet.nrows):
    #         cells = sheet.row_values(a)
    #         data = str(cells[i])
    #         dat.append(data)
    # return dat
    workbook = xlrd.open_workbook("C:\\Users\\Albert\\Desktop\\Nerve测试网节点奖励注册表.xlsx")
    sheet = workbook.sheet_by_name("Sheet1")
    nrows = sheet.nrows
    print(nrows)
    # cols = sheet.ncols
    dat = []
    for i in range(0, nrows):
        cells = sheet.col_values(1)
        data = str(cells[i])
        dat.append(data)
    return dat


b = excel()
# workbook1 = xlsxwriter.Workbook("C:\\Users\\Albert\\Desktop\\Nerve测试网节点奖励注册表.xlsx")
# worksheet = workbook1.add_worksheet("Sheet3")
# worksheet.write_column("C1", tx)
# worksheet.write_column("B1", b[15:24])
# worksheet.write_column("C1", b[27:36])
# worksheet.write_column("D1", b[39:48])
# workbook1.close()
print(b)

# def test(s):
#     for c in s:
#         if c is not None:
#             print(c)
#
#
# print(test(b))
