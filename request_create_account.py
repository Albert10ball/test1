# encoding = utf-8

import requests


url = "http://192.168.1.143:17004/jsonrpc"
headers = {"Content-Type": "application/json"}


def create(url, headers, count):

    formdata = {
        "jsonrpc": "2.0",
        "method": "createAccount",
        "params": [5, count, "nuls123456"],
        "id": "1234"
    }
    response = requests.post(url, json=formdata, headers=headers)

    address = response.json()["result"]
    return address


# address = create(url, headers, 4)
# print(address)
# lenth = len(address)
# print(lenth)
# for i in range(0, lenth):
#     print(address[i])







