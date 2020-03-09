# encoding=utf-8

member = [1, 2, 3, "nicek", ["baby", "乖乖"]]
a = len(member)
print(a)
member.append("炘岑")    #添加一个元素到列表末尾

print(member)
b = len(member)
print(b)
member.extend([2, 3, 5])    #已列表形式添加多个元素到列表末尾
print(member)

member.insert(2, "lin")    #在列表指定位置插入元素
print(member)
c = member[2]
print("c=", c)
