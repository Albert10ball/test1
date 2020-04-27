# encoding = utf-8


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s ' % (self.name, self.age))

    def get_age(self):
        if self.age >= 65:
            return "old man!"
        elif 18 <= self.age < 65:
            return "you are adult!"
        else:
            return "young!"


yi = Student("yizhonglin", 28)
yang = Student("yangxc", 27)
yi.print_age()
print(yang.get_age())
print(yang.age)
print(yang.name)



