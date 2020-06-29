# encoding = utf-8

import requests
import json
import request_create_account

url = "http://192.168.1.143:17004/jsonrpc"
headers = {"Content-Type": "application/json"}
sender = "TNVTdTSPVcqUCdfVYWwrbuRtZ1oM6GpSgsgF5"
passwd = "nuls123456"
amount = 1000000*1
remark = "test"
receiverR = request_create_account.create(url, headers, 4)
print(receiverR)


def transfer(url, headers, receiver):

    form_data = {
        "jsonrpc": "2.0",
        "method": "transfer",
        "params": [5, 5, 1, sender, receiver, passwd, amount, remark],
        "id": 1234
    }

    response = requests.post(url, json=form_data, headers=headers)

    # print(response.url)
    # print(response.text)
    # 如果是json文件可以直接显示
    # print(response.json())
    # print(type(response.json()))
    # response1 = response.json()
    print(response.json()["result"]["hash"])
    assert response.json()["result"]["hash"]
    return "Pass"


lenth = len(receiverR)
print(lenth)
for i in range(0, lenth):
    try:
        print(receiverR[i])
        print(transfer(url, headers, receiverR[i]))
    except BaseException as msg:
        print(msg)
# for i in range(0, 9000000):
#    print("第%d次转账:" % i)
#   post(url, headers)


