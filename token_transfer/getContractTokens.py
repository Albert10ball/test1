# encoding = utf-8
'''
@author: Albert
@contact:
@software: PyCharm
@file: getContractTokens.py
@time: 2020/09/01 上午 10:39
@desc:
'''

import requests
import time
import xlsxwriter
import math

url = "https://public1.nuls.io/jsonrpc"
headers = {"Content-Type": "application/json"}
contract = "NULSd6Hgvzkzkmc6b7c6hjjekuR4BasdG3twL"


def get_contract_tokens(url, headers, page, pagesize,  contract):
    from_data = {
        "id": 1234,
        "jsonrpc": "2.0",
        "method": "getContractTokens",
        "params": [1, page, pagesize, contract]
    }
    res = requests.post(url=url, headers=headers, json=from_data)
    # print(res.text)
    count = res.json()["result"]["totalCount"]
    pagesize = len(res.json()["result"]["list"])
    addressl = []
    balancel = []
    for a in range(0, pagesize):
        # print(a)
        address = res.json()["result"]["list"][a]["address"]

        balance = res.json()["result"]["list"][a]["balance"]/1000000
        addressl.append(address)
        balancel.append(balance)
    return addressl, count, balancel


def address():
    i = get_contract_tokens(url, headers, 1, 1, contract)[1]
    print(get_contract_tokens(url, headers, 1, 1, contract)[1])
    addresses = []
    balance = []
    pagesize = 10
    i = math.ceil(i/pagesize)
    print(i)
    for s in range(0, i):
        try:
            print(s)
            res = get_contract_tokens(url, headers, s+1, pagesize, contract)
            address1 = res[0]
            balance1 = res[2]
            addresses = addresses + address1

            balance = balance + balance1
            time.sleep(0.1)
        except BaseException as msg:
            print(msg)
    # addresses.pop(0)
    # balance.pop(0)
    # print(addresses)
    return addresses, balance


expenses = address()
expenses1 = expenses[0]
expenses2 = expenses[1]

# 需要写入的数据
workbook = xlsxwriter.Workbook('D:\\Company\\LCC\\LCC持有地址列表.xlsx')
worksheet = workbook.add_worksheet()
# 行列初始位置
row = 0
col = 0

worksheet.set_column("A:A", 46)  # 设置A列宽为46
worksheet.set_column("B:B", 15)  # 设置B列宽为15

worksheet.write_column(0, 0, "Address")
worksheet.write_column(0, 1, "Balance")

worksheet.write_column("A2", expenses1)
worksheet.write_column("B2", expenses2)


workbook.close()
