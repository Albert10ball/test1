# encoding = utf-8
import sys

sys.setrecursionlimit(10)
# 递归：函数内部调用自身的一种算法
'''
1、默认递归深度100
2、自定义递归深度
   import sys;
   sys.setrecursionlimit(5)


'''
'''
def recursion():
    return recursion()


print(recursion())

'''

# 递归求阶乘
# 非递归版本


def fac1(n):
    result = n
    for i in range(1, n):
        result *= i

    return result


num = int(input("请输入一个整数："))
res = fac1(num)
print("%d的阶乘是：%d" % (num, res))

# 递归版


def fac2(n):
    if n == 1:
        return 1
    else:
        return n * fac2(n - 1)


num = int(input("请输入一个整数："))
res = fac2(num)
print("%d的阶乘是：%d" % (num, res))
