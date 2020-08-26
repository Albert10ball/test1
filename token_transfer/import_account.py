# encoding = utf-8
__author__ = "Albert"
import requests

# url = "http://beta.api.nuls.io/jsonrpc"
url = "https://api.nuls.io/jsonrpc"
privateKey = "3cd31f613bbf090f459e6b8232e009bebd6242d95a43872365f6bcd40930faa7"
headers = {"Content-Type": "application/json"}


def import_account(url, headers, privateKey):
    from_data = {
        "jsonrpc": "2.0",
        "method": "importPriKey",
        "params": [1, privateKey, "nuls1234"],
        "id": 1234
    }

    res = requests.post(url=url, headers=headers, json=from_data)
    address = res.json()["result"]
    return address


try:
    a = import_account(url, headers, privateKey)
    if a == "NULSd6HgbES8NWewD8xvDPLw2RHFXyGckWc2C":
        print(a)
    else:
        print("Address is error！")

except BaseException as s:
    print(s)
