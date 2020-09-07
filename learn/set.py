# encoding=utf-8

num1 = [1, 2, 3, 4, 5, 5, 3, 1, 2, 0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)

print(temp)

num2 = list(set(num1))   # 先把列表转成集合，在用list转成列表
print(num2)


