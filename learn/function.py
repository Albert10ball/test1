# encoding = utf-8


def ffc1():
    print("This is my first function!")


def discount(price, rate):

    final_price = price * rate
    # 试图在函数内部修改全局变量old_price的值，但python会在内部创建一个局部变量
    old_price = 5
    print("这是局部变量old_price的值：", old_price)
    return final_price


old_price = float(input("请输入商品原价："))
rate = float(input("请输入折扣率："))
print("这是全局变量old_price的值：", old_price)
new_price = discount(old_price, rate)
print("这是优惠价：", new_price)

ffc1()

# 内嵌函数；global 关键字可以声明一个变量为全局变量：global count = 10
count = 4
print("初始全局变量count值：", count)


def fun1():
    print("这是第一个函数")
    global count
    count = 8
    print("这是函数内重新声明的全局变量：", count)

    def fun2():
        print("这是fun1()里面的内嵌函数！")
    fun2()


fun1()
print("最新全局变量count的值：", count)











