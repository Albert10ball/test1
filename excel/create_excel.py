# encoding = utf-8
__author__ = "Albert"

'''
Excel的两种写入方式
date：2020/08/14
'''


import xlsxwriter

# workbook = xlsxwriter.Workbook("hello.xlsx")
# worksheet = workbook.add_worksheet()
#
# worksheet.write('A1', 'Hello,Yi')
# workbook.close()

workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# 需要写入的数据
expenses = (
    ['Name', 'Age', 'Address'],
    ['Yizhonglin', '27', 'ShaPingBa'],
    ['Mawuxuan', '25', 'Ranjiaba'],
    ['Zhuyou', '26', 'Ranjiaba'],
    ['Luopeng', '26', 'Daping']
)

# 行列初始位置
row = 0
col = 0

# .write方法 write(行，列，写入内容，样式)
for item, cost, ist in (expenses):

    worksheet.write(row, col, item)
    worksheet.write(row, col+1, cost)
    worksheet.write(row, col+2, ist)
    row +=1


worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B2:B5)')
workbook.close()

# 需要写入的数据
expenses1 = (
    ['Name', 'Yizhonglin', 'Mawuxuan', 'Zhuyou', 'Luopeng'],
    ['Age', '27', '25', '26', '26'],
    ['Address', 'ShaPingBa', 'Ranjiaba', 'Ranjiaba', 'Daping'],
)


workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()
# 行列初始位置
row = 0
col = 0

worksheet.write_column("E10", expenses1[0])
worksheet.write_column("F10", expenses1[1])
worksheet.write_column("G10", expenses1[2])

workbook.close()





