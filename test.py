# encoding =utf-8


import unittest
import time
import datetime
import requests
from time import strftime

# class test_1(unittest.TestCase):
#
#     def test_test1(self):
#         self.assertEqual(abs(-20), 20)
#         # self.assertEqual(abs(-2), 3)
#
#
# if __name__ == '__main__':
#     unittest.main()

print(time.ctime())
print(int(time.time()))

url = "https://api.nuls.io/jsonrpc"
header = {"Content-Type": "application/json"}


def get_lastblock(url, header):

    form_data ={
        "jsonrpc": "2.0",
        "method": "getBestBlockHeader",
        "params": [1],
        "id": 1234
    }
    response = requests.post(url=url, json=form_data, headers=header)
    # print(response.text)
    return response.json()


response = get_lastblock(url, header)
height1 = response["result"]["height"]
block = 2620000 - height1
print(block)
for i in range(0, block):

    res = get_lastblock(url, header)
    height = res["result"]["height"]
    ctime = res["result"]["time"]
    cha = 2620000 - height
    time1 = (cha * 10)
    time2 = int(time.time())
    now = datetime.datetime.now()
    t = time1 + time2
    timeArray = time.localtime(t)
    print("当前区块时间为：", ctime)
    print("当前NULS主网高度为：%d" % height)
    print("预计快照主网高度为：2620000")
    print("预计快照时间为：", time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
    print("*****************************************")
    time.sleep(10)
