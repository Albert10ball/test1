# encoding = UTF-8
# 字符串格式化

lin = "{0} love {1} {2}".format("I", "you", "yxc")
print(lin)
lin = "{a} love {b} {c}".format(b="I", a="you", c="yxc")
print(lin)
lin = "{0} love {b} {c}".format("I", b="you", c="yxc")
print(lin)
print("\ta")
print("\\")
# 冒号（:）字符串格式化的标志

''' 列表、元组和字符串共同点（三个统称为序列）
   1、都可以通过索引得到某个元素
   2、默认索引值都是从0开始
   3、可以通过分片的方式得到某一段元素的集合
   4、有很多共同的操作符（重复操作符*、拼接操作符+、成员关系操作符in或not in）
'''
a = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(list(a))
print(type(a))
a = str(a)
print(a)
print(type(a))
a = list(a)
print(type(a))


def function1():
    tuple1 = (2, 3, 25, 6, 52, 12, 51, 45)
    max1 = tuple1[0]
    print("max1 = ", max1)
    c1 = len(tuple1)
    print("c1=", c1)
    j = 1
    k = 1
    for each in tuple1:
        i = 1
        while i <= c1:
            i = i + 1
            k += 1
            if each > max1:
                j += 1
                max1 = each
                print("更换最大值：", j, ":", max1)

            else:
                continue
        print("max", k, ":", max1)
    return max1


c = function1()
print(c)


num = (2, 3, 25, 6, 52, -34, 12, 51, 45)
pp = enumerate(num)
print(list(pp))
a = (3, 2, 31, 44, 1, 4, 11, 45)
b = (21, 22, 4, 23, 131)
zip1 = zip(a, b)
print(list(zip1))
print(list(zip(b, a)))
print(1)



