# encoding = utf-8


def ds(x):
    return x * 2 + 1


print(ds(5))

# lambda 表达式
l1 = lambda x: 2 * x + 1
print(l1(2))
l2 = lambda x, y: x * y
print(l2(4, 7))

# lambda表达式的作用：调用率低的函数方法，不考虑命名问题，简化代码可读性

# 两个牛逼的BIF（内置函数）
# filter()


def add(x):
    return x % 2


temp = range(10)
show = filter(add, temp)
print(list(show))

print("filter():", list(filter(lambda x: x % 2, range(20))))

# map()

print("map():", list(map(lambda x: x / 2, range(10))))



