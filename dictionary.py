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

