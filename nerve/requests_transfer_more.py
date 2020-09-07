# encoding = utf-8

import requests
import json

url = "http://192.168.1.128:17004/jsonrpc"
headers = {"Content-Type": "application/json"}
sender = "TNVTdTSPVcqUCdfVYWwrbuRtZ1oM6GpSgsgF5"
passwd = "nuls1234"
amount = 100000000*300000
amount2 = 100000000*10
remark = "test"
# receiverR = request_create_account.create(url, headers, 4)
# receiverR = ["TNVTdTSPLP5gQytCMSb6g3KRtcD4n8ZGx8otx", "TNVTdTSPRyJgExG4HQu5g1sVxhVVFcpCa6fqw",
#              "TNVTdTSPMr3X7MUGejv7ns8WEyZGGY59AsB6V", "TNVTdTSPFy4PpZGxFeXYCteth5yDvkVZw7q8d",
#              "TNVTdTSPEjHtAsQJL52SfaN4mthMzFFfy2GKJ", "TNVTdTSPFcSv8gdTQn95ZH9bM6Loi6GMg4id3",
#              "TNVTdTSPEoVRZJ9VLZa92hGFDNc2hA32UnH6A", "TNVTdTSPRyfpfEJAKyK7pzdLCFGqoyLeSYKsv",
#              "TNVTdTSPR2MwyeSioJ4U2raKWYMWCtJp4sBw2", "TNVTdTSPUbsMCmExtuesWezipSvoWtUC9PB1o",
#              "TNVTdTSPHWdWuHZvf32VN3Xk6RwHkRxFa5iuz", "TNVTdTSPRRH3uceFUeo4itpki9UJvg3fDZ6FM",
#              "TNVTdTSPKqhRBVCVSnJaSHhxFzLkN6Sm9yZ6T", "TNVTdTSPGjdspncjLiGc4mJ15eLMnX25djdot",
#              "TNVTdTSPVxQFsiMYyzjVgZdpMGrfzWS1bepLS", "TNVTdTSPRYKWQbwF8qUr2FbGS6Ju9nzYj3ptj",
#              "TNVTdTSPSeAoWmZFFHCeYzAXCYYaDEVS4BvVh", "TNVTdTSPTwEY9FbHKPYe4gQxbQGU7WV7LdT74",
#              "TNVTdTSPEgem44Rihm3Dfcjt2JsQj8Gv7Ti5d", "TNVTdTSPQEVWufkCc3VohR6rkpAdyUeR7aLwB",
#              "TNVTdTSPGQc9eSCkUbnwVyJuBCaM4Zj2PVpvN", "TNVTdTSPNANf4E2b5xCTp8GJ8Cr2x7bk5Rgcf",
#              "TNVTdTSPHJLKmt4PV97Uik98XfRziRYzQZihu", "TNVTdTSPJ6woewNz5XdaT35KCGRp5YXQ4mkfX",
#              "TNVTdTSPQpDjXBekoTSJE8M4jtzrkz5p3HA89", "TNVTdTSPM2zQmR8UkuYd9ZRfG7uDPGKjpSBvF",
#              "TNVTdTSPKXcH2Vu4uDWobS4H9o3YadH5hv2KR", "TNVTdTSPJYQnTobMK2XNgU8L4wsqFUy1irYQS",
#              "TNVTdTSPEn3kK94RqiMffiKkXTQ2anRwhN1J9", "TNVTdTSPEoVRZJ9VLZa92hGFDNc2hA32UnH6A",
#              "TNVTdTSPGQeHfn5U31nxSqSMP8KSwDNG2qWGF", "TNVTdTSPVf5iJ4f42B48B95kY5rWzSUAcbv19",
#              "TNVTdTSPMWFxjAkC44yy1siKtejoALes9xTL9", "TNVTdTSPQkaer2rYwvZy14A8N5omH67o3DVs3"]

receiverR = [ "TNVTdTSPUk4eFCJNFjBYHwxGvuiq8fcRFqvv3", "TNVTdTSPHJGCfgFkQVW1z7BB1seYsRLUX8D4C",
              "TNVTdTSPTfWYDyM3C6DqLGpRtezzPcKWdvjbR", "TNVTdTSPMaHzALJprL6xduu29pVmBg2iQYcE3",
              "TNVTdTSPJFUZgSvDJQ8isfd7Q2xpq7ZvGsEap"]
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
    print(response.text)
    # 如果是json文件可以直接显示
    # print(response.json())
    # print(type(response.json()))
    # response1 = response.json()
    print(response.json()["result"]["hash"])
    assert response.json()["result"]["hash"]
    return "Pass"


def transfer2(url, headers, receiver):

    form_data = {
        "jsonrpc": "2.0",
        "method": "transfer",
        "params": [5, 2, 1, sender, receiver, passwd, amount2, remark],
        "id": 1234
    }

    response = requests.post(url, json=form_data, headers=headers)

    # print(response.url)
    print(response.text)
    # 如果是json文件可以直接显示
    # print(response.json())
    # print(type(response.json()))
    # response1 = response.json()
    print(response.json()["result"]["hash"])
    assert response.json()["result"]["hash"]
    return "Pass"

lenth = len(receiverR)
# print(lenth)
# for i in range(0, lenth):
#     try:
#         print(receiverR[i])
#         print(transfer(url, headers, receiverR[i]))
#     except BaseException as msg:
#         print(msg)
for i in range(0, lenth):
    try:
        print(receiverR[i])
        print("第%d次转账:" % i)
        print(transfer(url, headers, receiverR[i]))
        print(transfer2(url, headers, receiverR[i]))
    except BaseException as msg:
        print(msg)



