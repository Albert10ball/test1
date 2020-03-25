# encoding = utf-8

'''
将汉诺塔简单分为3个步骤：
1、将前63个盘子从X移动到Y上
2、将最底上的第64个盘子从X移动到Z上
3、将Y上面的63个盘子移动到Z上

问题：
1、将X上的63个盘子借助Z移动到Y上
2、将Y上的63个盘子借助X移动到Z上

两个问题反复循环，直至最后盘子为0
'''


def hannoi(n, x, y, z):
    if n == 1:
        print(x, "-->", z)
    else:
        hannoi(n-1, x, z, y)    # 将前n-1个盘子从x移动到y上
        print(x, "-->", z)      # 将最底下的一个盘子从x移动到z上
        hannoi(n-1, y, x, z)    # 将y上面的n-1个盘子通过x移动到z上


n = int(input("请输入汉诺塔层数n值："))
print(hannoi(n, 'X', 'Y', 'Z'))




