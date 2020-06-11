# encoding=utf-8

n1 = int(input("请输入虚拟银行抵押的NVT数量："))
n2 = int(input("请输入共识节点抵押的NVT数量："))
n3 = int(input("请输入抵押的活期NVT数量："))
n4 = int(input("请输入抵押的三个月NVT数量："))
n5 = int(input("请输入抵押的半年NVT数量："))
n6 = int(input("请输入抵押的一年NVT数量："))

ns = float(input("请输入NULS/NVT的价格："))

s0 = int(input("请输入抵押的活期NULS数量："))
s1 = int(input("请输入抵押的三个月NNULS数量："))
s2 = int(input("请输入抵押的半年NULS数量："))
s3 = int(input("请输入抵押的一年NULS数量："))


def sqrt(num):

    r = num ** 0.5
    return r


value_nvt = n1 * sqrt(2*4) + n2 * sqrt(2*3) + n3 * sqrt(2*1) + n4 * sqrt(2*1.2) + n5 * sqrt(2*1.5) + n6 * sqrt(2*2)

value_nuls = (s0 * sqrt(2*1) + s1 * sqrt(2*1.2) + s2 * sqrt(2*1.5) + s3 * sqrt(2*2)) * ns
value = value_nuls + value_nvt
per = 86400 / value

nvt_rate1 = per * sqrt(2*4) * 365
print("虚拟银行抵押NVT年利率为：%.2f%%" % (nvt_rate1 * 100))
nvt_rate2 = per * sqrt(2*3) * 365
print("共识节点抵押NVT年利率为：%.2f%%" % (nvt_rate2 * 100))
print("")
nvt_rate3 = per * sqrt(2*1) * 365
print("NVT活期抵押年利率为：%.2f%%" % (nvt_rate3 * 100))
nvt_rate4 = per * sqrt(2*1.2) * 365
print("NVT抵押三个月年利率为：%.2f%%" % (nvt_rate4 * 100))
nvt_rate5 = per * sqrt(2*1.5) * 365
print("NVT抵押半年年利率为：%.2f%%" % (nvt_rate5 * 100))
nvt_rate6 = per * sqrt(2*2) * 365
print("NVT抵押一年年利率为：%.2f%%" % (nvt_rate6 * 100))
print("")
nuls_rate1 = per * sqrt(2*1) * 365 * ns
print("NULS活期抵押年利率为：%.2f%%" % (nuls_rate1 * 100))
nuls_rate2 = per * sqrt(2*1.2) * 365 * ns
print("NULS抵押三个月年利率为：%.2f%%" % (nuls_rate2 * 100))
nuls_rate3 = per * sqrt(2*1.5) * 365 * ns
print("NULS抵押半年年利率为：%.2f%%" % (nuls_rate3 * 100))
nuls_rate4 = per * sqrt(2*2) * 365 * ns
print("NULS抵押一年年利率为：%.2f%%" % (nuls_rate4 * 100))




