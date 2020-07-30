# encoding=utf-8
import random


def function1(str1):
    print(str1)
    return


a1 = random.randint(1, 10)
while a1 > 5:
    function1(input("请输入一个数："))
    print("结束！")
    break
else:
    a1 = random.randint(30, 100)
    print(a1)
    print("again!")
