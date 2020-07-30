# encoding = utf-8
import sys


# Fibonacci 数列

# 递归算法
# 递归相当于迭代，参数越大效率越来越低

def fib1(n):
    if n < 1:
        print("输入错误，不能小于1！")
        return -1
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        res = fib1(n-1) + fib1(n-2)
        return res


n = int(input("请输入n值："))
result = fib1(n)
if result != -1:
    print("一共有%d对兔子！" % result)





