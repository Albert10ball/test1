# encoding=utf-8

lin = int(8)
print(type(lin))
ling = int(input("请输入一个我心中想的数字："))
print(type(ling))
while True:
    if ling == lin:
        break
    elif ling > lin:
        ling = int(input("不好意思太大了，请重新输入"))
    elif ling < lin:
        ling = int(input("不好意思太小了，请重来："))
print("真棒，竟然被你猜到了！")

