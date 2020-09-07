# encoding=utf-8

import os


print(os.getcwd())

print(os.listdir("D:\\"))

os.mkdir("D:\\appso")
print(os.listdir("D:\\"))


def create_txt(name, msg):
    desktop_path = "D:\\appso\\"
    full_path = desktop_path + name + ".txt"
    file = open(full_path, "w")
    file.write(msg)
    file.close()


create_txt("yzl_test", "Hello lin!")


print(os.path.basename("D:\\aapso\\yzl_test.txt"))
f = open("D:\\appso\\yzl_test.txt", "r+")
print(f.read())
f.close()
os.remove("D:\\appso\\yzl_test.txt")

os.renames("D:\\appso", "D:\\appIPP")
print(os.listdir("D:\\"))
print(os.path.dirname("D:\\aapIPP\\yzl_test.txt"))
os.remove("D:\\appIPP")
print(os.listdir("D:\\"))


print(os.path.join("D:\\", "A", "B", "C"))





