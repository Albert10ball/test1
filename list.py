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

