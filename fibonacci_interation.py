# encoding = utf-8
import sys


# Fibonacci 数列
# 迭代算法

def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print("输入错误，不能小于1！")
        return -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3


n = int(input("请输入n值："))
res = fib(n)
if res != -1:
    print("一共有%d只兔子！" % res)




