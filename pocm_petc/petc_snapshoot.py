# encoding = utf-8
'''
@author: Albert
@contact:
@software: PyCharm
@file: createAccount.py
@time: 2020/09/17 15：30
@desc:获取pocm项目的参与列表并写入excel
'''

import requests
import json
import xlsxwriter
import math
import time

url = "https://pocm.nuls.io/api/pocm/participant/list"
headers = {"Content-Type": "application/json"}


def list(url, headers):
    in_data = {
        "releaseId": 46
    }
    response = requests.post(url=url, json=in_data, headers=headers)
    address = []
    amount = []
    time4 = []
    data = response.json()["data"]
    lenth = len(data)
    for i in range(0, lenth):
        address1 = data[i]["depositAddress"]
        amount1 = float(data[i]["depositAmount"])/100000000
        up_time = data[i]["updateTime"]/1000
        time1 = time.localtime(up_time)
        ut = time.strftime("%Y-%m-%d %H:%M:%S", time1)
        address.append(address1)
        amount.append(amount1)
        time4.append(ut)
    return address, amount, time4


res = list(url, headers)
address = res[0]
amount = res[1]
time2 = res[2]


print("**************************PETC***************************")
print("PETC项目参与者第一次快照完成！")

# 需要写入的数据
cdate = str(time.strftime("%Y%m%d %H:%M:%S"))[:8]
print(('D:\\PetChain项目\\Air-drop\\PETC项目参与者快照' + cdate + '.xlsx'))
workbook = xlsxwriter.Workbook('D:\\PetChain项目\\Air-drop\\PETC项目参与者快照' + cdate + '.xlsx')
worksheet = workbook.add_worksheet()
s = len(time2)
snap_date = [time.ctime()]*s
print(snap_date)

# 行列初始位置
row = 0
col = 0
worksheet.set_column("A:A", 25)  # 设置B列宽为15
worksheet.set_column("B:B", 39)  # 设置A列宽为46
worksheet.set_column("C:C", 6.5)  # 设置B列宽为15
worksheet.set_column("D:D", 20)  # 设置B列宽为15

worksheet.write_column(0, 0, ["快照时间"])
worksheet.write_column(0, 1, ["地址"])
worksheet.write_column(0, 2, ["数量"])
worksheet.write_column(0, 3, ["最近参与时间"])

worksheet.write_column("A2", snap_date)
worksheet.write_column("B2", address)
worksheet.write_column("C2", amount)
worksheet.write_column("D2", time2)

workbook.close()




