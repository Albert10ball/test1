# encoding = utf-8
__author__ = "Albert"

import requests
import time

# url = "http://beta.api.nuls.io/jsonrpc"
# fromAddress = "tNULSeBaMkhLBvnWx8jTSoCCbuDwhza6hSMYw9"
# contractAddress = "tNULSeBaN5n4F6anbRsAqvyfYqm3FA68XnSDQp"
# amount = 1000000000

url = "https://api.nuls.io/jsonrpc"
fromAddress = "NULSd6HgbES8NWewD8xvDPLw2RHFXyGckWc2C"
contractAddress = "NULSd6Hgvzkzkmc6b7c6hjjekuR4BasdG3twL"
amount = 50*1000000

headers = {"Content-Type": "application/json", 'Connection': 'close'}

# receivers = ["tNULSeBaMqz4YPhN7QH3XHYjS1uNzETU4214Uq", "tNULSeBaMoypAn7zXEkjX59bWR2BGrJUjJCUD9",
#              "tNULSeBaMrnz12BDcpY9vZZ8LQJqK93D7ypwco"]

receivers = ["NULSd6HgeR4L2wdiqRf1WMhowQNuPAF4KErYC",
             "NULSd6HgVL5YvG6XeftaabcBGfsLSRoo2W7YE"]


def token_transfer(url, headers, receiver):
    from_data = {
        "jsonrpc": "2.0",
        "method": "tokentransfer",
        "params": [1, fromAddress, "nuls1234", receiver, contractAddress, amount, "LCC Air-drop!"],
        "id": 1234
    }

    res = requests.post(url=url, headers=headers, json=from_data)
    print(res.json()["result"]["txHash"])
    return "Pass"


lenth = len(receivers)
for i in range(0, lenth):
    try:
        print("第%d次转账：" % i)
        token_transfer(url, headers, receivers[i])
        time.sleep(0.5)
    except BaseException as s:
        print(s)




