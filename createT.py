# encoding=utf-8
import time
import string
import random


num = random.randint(1, 200)
temp = input("请输入你猜想的数字：")
guess = int(temp)
while guess != num:
    temp = input("请重新输入数字：")
    guess = int(temp)
    if guess == num:
        print("这么厉害吗，竟然猜到了！")
    else:
        if guess > num:
            print("大了大了，没猜中哦！")
        else:
            print("不好意思，猜小了！")
print("这个数是：")
print(num)
print("游戏结束，不玩了")
