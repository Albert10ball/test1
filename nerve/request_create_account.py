# encoding = utf-8

import requests


url = "https://api.nuls.io/jsonrpc"
headers = {"Content-Type": "application/json"}


def create(url, headers, count):

    formdata = {
        "jsonrpc": "2.0",
        "method": "createAccount",
        "params": [1, count, "albert@321"],
        "id": "1234"
    }
    response = requests.post(url, json=formdata, headers=headers)
    print(response.text)
    address = response.json()["result"]
    return address


def main():
    try:
        address = create(url, headers, 100)
        # print(address)
        lenth = len(address)
        # print(lenth)
        for i in range(0, lenth):
            str1 = address[i]
            str2 = str1[-3:]
            if str2 == "lin" or str2 == "Lin":
                print(str2)
                print(str1)
                break
            # else:
            #     print(str2)
    except BaseException as g:
        print(g)


for s in range(0, 1000000):
    main()




