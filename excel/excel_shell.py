# encoding = utf-8
__author__ = "Albert"


import xlsxwriter

workbook = xlsxwriter.Workbook("chart.xlsx")
worksheet = workbook.add_worksheet("sheet1")

# 需要写入的数据
expenses = (
    ['Name', 'Age', 'Num', 'Address'],
    ['Yizhonglin', 27, 'ShaPingBa'],
    ['Mawuxuan', 25, 'Ranjiaba'],
    ['Zhuyou', 26, 'Ranjiaba'],
    ['Luopeng', 26, 'Daping']
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

# 新建图表格式 line为折线图
chart_col = workbook.add_chart({'type': 'line'})
chart_col.add_series(
    {
        "name": '=sheet1!$B$1',
        "categories": '=sheet1!$A$2:$A$5',
        "values": '=sheet1!$B$2:$B$5',
        'line': {'color': 'green'}
    }
)

chart_col.set_title({'name': '年龄表'})
chart_col.set_x_axis({'name': '姓名'})
chart_col.set_y_axis({'name': '年龄'})

chart_col.set_style(1)

worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})
workbook.close()
