# encoding = utf-8
__author__ = "Albert"


import time
from nerve import search

print(time.ctime())
print(time.localtime())

time1 = str(time.strftime("%Y%m%d %H:%M:%S"))[:8]
print(time1)
print(search.search("3000").json()["result"]["type"])


