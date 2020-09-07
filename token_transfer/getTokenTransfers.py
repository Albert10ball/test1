# encoding = utf-8
__author__ = "Albert"

import xlsxwriter
import requests
import math, time

url = "https://public1.nuls.io/jsonrpc"
headers = {"Content-Type": "application/json"}
contract = "NULSd6Hgvzkzkmc6b7c6hjjekuR4BasdG3twL"
address = "NULSd6HgbES8NWewD8xvDPLw2RHFXyGckWc2C"


def get_token_transfers(url, headers, page, pagesize, address, contract):
    from_data = {
        "id": 1234,
        "jsonrpc": "2.0",
        "method": "getTokenTransfers",
        "params": [1, page, pagesize, address, contract]
    }
    res = requests.post(url=url, headers=headers, json=from_data)
    # print(res.text)
    count = res.json()["result"]["totalCount"]
    lenth = len(res.json()["result"]["list"])
    print(lenth)
    address_list = []
    value = []
    for i in range(0, lenth):
        # print(pagesize)
        # print(i)
        address1 = res.json()["result"]["list"][i]["toAddress"]
        value1 = float(int(res.json()["result"]["list"][i]["value"])/1000000)
        address_list.append(address1)
        value.append(value1)
    return count, address_list, value


def getlist():
    addresses = []
    values = []
    count = get_token_transfers(url, headers, 1, 1, address, contract)[0]
    pagesize = 100
    page = math.ceil(count/pagesize)
    for a in range(1, page+1):
        try:
            print(a)
            res1 = get_token_transfers(url, headers, a, pagesize, address, contract)
            address12 = res1[1]
            value12 = res1[2]
            addresses = addresses + address12
            values = values + value12
        except BaseException as b:
            print(b)
    return addresses, values


expecse = getlist()
address3 = expecse[0]
value3 = expecse[1]
# 需要写入的数据
workbook = xlsxwriter.Workbook('D:\\Company\\LCC\\LCC空投发放记录.xlsx')
worksheet = workbook.add_worksheet("LCC发放记录表")
# 行列初始位置
row = 0
col = 0
worksheet.write_column("A1", "地址")
worksheet.write_column("B1", "数量")

worksheet.set_column("A:A", 46)  # 设置A列宽为46
worksheet.set_column("B:B", 5)  # 设置B列宽为5
worksheet.write_column("A2", address3)
worksheet.write_column("B2", value3)


workbook.close()

