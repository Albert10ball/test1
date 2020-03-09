# encoding=utf-8

import random

from pip._vendor.distlib.compat import raw_input

a1 = int(raw_input("请输入购买彩票注数："))

for i in range(0, a1):
    alis = random.sample(range(1, 34), 6)
    B = random.randint(0, 15)
    print("第", i + 1, "注：", alis, ", [", B + 1, "]")
