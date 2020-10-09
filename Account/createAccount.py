# encoding = utf-8
'''
@author: Albert
@contact:
@software: PyCharm
@file: createAccount.py
@time: 2020/09/08 14：30
@desc:JsonRpc接口和restful接口创建地址
'''

import requests
import json

url = "http://beta.api.nuls.io/"
headers = {"Content-Type": "application/json"}


def create_account_jsonrpc(url, headers, count):
    from_data = {
        "jsonrpc": "2.0",
        "id": 1234,
        "method": "createAccount",
        "params": [2, count, "nuls1234"]
    }
    url1 = url + "jsonrpc"
    response = requests.post(url=url1, headers=headers, json=from_data).json()
    return response


def create_account_restful(url, headers, count):
    data = {
        "count": count,
        "prefix": "tNULS",
        "password": "nuls1234"
    }
    url1 = url + "api/account"
    response = requests.post(url1, headers=headers, json=data).json()
    return response


print(create_account_jsonrpc(url, headers, 5))
print(create_account_restful(url, headers, 5))




