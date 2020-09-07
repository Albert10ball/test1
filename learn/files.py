# encoding=utf-8

f = open('D:\\tool\\python_learn.txt')
print(f)

# print(f.read())
print(f.read(10))

print(f.tell())
f.close()
f = open('D:\\tool\\python_learn.txt', 'w')

f.write("今天天气是真的太棒了！")
f.close()
s = f.readline()

print(s)


