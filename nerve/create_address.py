# encoding = utf-8

import requests

url = "http://api.nerve.network/jsonrpc"
headers = {"Content-Type": "application/json"}


def create(url, headers, count):

    formdata = {
        "jsonrpc": "2.0",
        "method": "createAccount",
        "params": [9, count, "albert@321"],
        "id": "1234"
    }
    response = requests.post(url, json=formdata, headers=headers)
    print(response.text)
    address = response.json()["result"]
    return address


try:
    ad = create(url, headers, 10)
    lenth = len(ad)
    # print(lenth)
    for i in range(0, lenth):
        print(ad[i])
except BaseException as s:
    print(s)


