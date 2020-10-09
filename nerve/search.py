# encoding = utf-8
'''
@author: Albert
@contact:
@software: PyCharm
@file: getContractTokens.py
@time: 2020/09/02  16:40
@desc: 用于Nerve网络查询单个交易、地址、区块
'''

import requests
url = "https://scan.nerve.network/api/"
headers = {"Content-Type": "application/json"}


def search(input):
    from_data = {
        "id": 1234,
        "jsonrpc": "2.0",
        "method": "search",
        "params": [9, input]
    }
    res = requests.post(url="https://scan.nerve.network/api/", headers={"Content-Type": "application/json"},
                        json=from_data)
    return res


# print(search("123").json()["result"]["type"])
# print(search("NERVEepb6CY4q799Pqk3dKuxZgU68Hn8WpPdEE").json()["result"]["type"])
# print(search("b031ed42c14859cbce8a0816bfee30f2fd5df60ccf500e0efb27c999ebf4d6fd").json()["result"]["type"])
# print(search("3b0c81b09667b2d059d5ff394e9c630b18d659b1267bab67dc8560ac965733e9").json()["result"]["type"])



