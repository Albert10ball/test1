# encoding = utf-8
# 一一映射
brand = ['李宁', '耐克', '阿迪达斯', '安踏']
slogn = ['一切皆有可能', 'just do it', 'nothing is impossible', '动起来']
print("耐克的口号是：", slogn[brand.index("耐克")])

# dictionary 字典的使用
dict1 = {'李宁': '一切皆有可能', '耐克': 'just do it', '阿迪达斯': 'nothing is impossible', '安踏': '动起来'}
print("李宁的口号是：", dict1["李宁"])
print(dict1)

# 元组变字典
dict2 = dict(((1, "I"), (2, "l"), (3, "o"), (4, "v"), (5, "e"), (6, "y"), (7, "o"), (8, "u")))
print(dict2)
print(dict2[1], dict2[2])

dict2 = dict(yi="天气好", zhong="明天下雨", lin="大太阳")
print(dict2)
dict2["yi"] = "天气不好了"    # 修改字典
print(dict2)
dict2["20"] = "雷阵雨来了哦"  # 增加内容
print(dict2)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


# BMI公式
# print("特制身体BMI计算器！")
# h = float(input("请输入身高（cm）:"))
# w = float(input("请输入体重（kg）:"))
# h1 = h/100
# h2 = h1*h1
# BMI = w/h2
# if BMI <= 18.5:
#     print("你的BMI指数为：%.2f，属于偏低，营养不良，请多补充营养！" % BMI)
# elif 18.5 < BMI <= 25:
#     print("你的BMI指数为：%.2f，属于正常，棒棒哒，perfect！" % BMI)
# elif 25 < BMI <= 28:
#     print("你的BMI指数为：%.2f，属于过重，营养过多，请注意减少能量摄入，多运动运动！" % BMI)
# elif 28 < BMI < 32:
#     print("你的BMI指数为：%.2f，属于肥胖，营养太多，不能再吃了，快去运动吧！" % BMI)
# else:
#     print("你的BMI指数为：%.2f，属于严重肥胖，营养爆炸，建议绝食！" % BMI)


# 字典的自建函数

dict1 = {}
print(dict1.fromkeys((1, 2, 3)))
print(dict1.fromkeys((1, 2, 3), "a"))
dict1 = {}
dict2 = dict1.fromkeys(range(4), "string")
print(dict2)

for eachKey in dict2.keys():
    print(eachKey)

for eachValue in dict2.values():
    print(eachValue)

for eachItem in dict2.items():
    print(eachItem)

print(dict2[2], dict2.get(2))

print(dict2.get(5, "不存在"))
print(dict2.get(3, "不存在"))
print(32 in dict2)
print(3 in dict2)
dict2.clear()
print(dict2)

# 字典清空方法：clear方法和直接赋值为{}

a = {2: "三"}
b = a
print("字典a=", a)
print("字典b=", b)
a = {}
print("字典a=", a)
print("字典b=", b)

a = b
print("字典a=", a)
print("字典b=", b)
b.clear()
print("字典a=", a)
print("字典b=", b)

a = {1: "one", 2: "two", 3: "three", 4: "four"}
b = a.copy()
c = a

print(a, "\n", b, "\n", c, "\n", id(a), "\n", id(b), "\n", id(c))
print(a.pop(2))    # 弹出指定位置的一个元素
print(a)
print(a.popitem())    # 随机弹出字典中的一个元素
print(a)
a = {1: "one", 2: "two", 3: "three", 4: "four"}
print(type(a))
a = a.setdefault(6, "三")
a = {1: "one", 2: "two", 3: "three", 4: "four"}
print(a)
print(type(a))

b = {3: "tree"}
a.update(b)
print(type(a))
print(a)




