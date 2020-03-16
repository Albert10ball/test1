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

list3 = list1 + list2
print(list3)

list4 = list3*3
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









