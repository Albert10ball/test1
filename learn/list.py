# encoding=utf-8

member = [1, 2, 3, "nicek", ["baby", "乖乖"]]
a = len(member)
print(a)
member.append("炘岑")    # 添加一个元素到列表末尾

print(member)
b = len(member)
print(b)
member.extend([2, 3, 5])    # 已列表形式添加多个元素到列表末尾
print(member)

member.insert(2, "lin")    # 在列表指定位置插入元素
print(member)
c = member[2]
print("c=", c)
# 调换元素“lin”和元素“3”的位置
temp = member[2]
member[2] = member[3]
member[3] = temp
print(member)

member.remove(2)     # remove移除list中的元素
print(member)

member.pop()        # pop移除list中最后一个元素
print(member)

member.pop(0)        # pop移除list中指定位置的一个元素
print(member)

# 索引列表
member1 = member[:2]
print(member1)
member2 = member[2:]
print(member2)


list1 = [234]
list2 = [567]
if list1 < list2:
    print(1)
else:
    print(2)

list1 = list1 + list2
print(list1)

list4 = list1*3
print(list4)

t1 = "lin" not in list4
print(t1)

t2 = "lin" in list4
print(t2)
list5 = [[1, 2, 3], [2, 3, 4], 1, 4, 5]
a1 = list5[1][1]
a3 = list5[1]
print(a1, a3)
a2 = list5[3]
print(a2)
print(list5.count(1))   # 元素在list中出现的次数
print(list5.index(4))  # 元素在list中的位置 index（a, b, c） a为元素，bc为位置范围

list5.reverse()    # 反转列表
print(list5)
list6 = [3, 4, 1, 2, 44, 5, 8]
list6.sort()     # 列表排序(正序)
print(list6)
list6.sort(reverse=True)  # 列表排序（倒序）
print(list6)
list7 = list6[:]   # 分片copy list6 与list7 = list6 的区别在于指向的对象列表不是同一主体
print(list7)
print(1111)
# print("hello""\n", d1)

# 元组（tuple）与list的区别
'''
1、元组对象不可更改
2、元组的关键是逗号（，）分割 比如：tuple = (1,)
3、8 * (8) = 64,  8 * (8,) = (8, 8, 8, 8, 8, 8, 8, 8)
4、元组操作 拼接符（+）、重复符（*）、
'''
# 元组中插入元素
temp1 = ("一心", "一意", "太多", "太少")
temp1 = temp1[:2] + ("lin", ) + temp1[2:]
print(temp1)

# 字符串内置操作方法
str1 = "My love is xing!"
print(str1[:6])
print(str1[3])
str1 = str1[:7] + " first" + str1[7:]
print(str1)

str2 = "spring"
str2 = str2.capitalize()   # 字符串首字母改为大写
print(str2)

str2 = "SPRINsG"
str2 = str2.casefold()    # 字符在中所有大写改为小写
print(str2)

str3 = str2.center(40)   # 字符串居中
print(str3)

num = str2.count("s")   # 字符或字符串在字符串中出现的次数统计
print(num)
print(str2.endswith("si"))
print(str2.endswith("sg"))


print(str2.find("dds"))
print(str2.find("in"))

print(str2.join("12112"))


str2 = "       I love you yxc"
print(str2)
print(str2.lstrip())


str2 = "kjkjsjkhkksio"   # 将字符串隔成3个字符串组成一个元组
str2 = str2.partition("js")
print(str2)

str2 = "I love you yxc"
str2 = str2.replace("yxc", "xxx")
print(str2)
print(str2.index("ov"))
print(str2.rindex("o"))

str2 = "  I love you   !   "
print(str2.split("o"))    # 根据参数把字符串切成list，参数为空时，以空格为切点
print(str2.strip())      # 去掉字符串左右两边的空格

str2 = "My love is yxc, you know?"
print(str2.translate(str2.maketrans("o", "0")))  # 用0替换掉字符串中所有的o
print(str2.maketrans("o", "-"))

