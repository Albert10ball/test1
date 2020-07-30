# encoding = utf-8


class Student(object):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def print_age(self):
    #     print('%s: %s ' % (self.name, self.age))

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def private_variable(self):
        print('%s: %s' % (self.__name, self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_age1(self):
        if self.__age >= 65:
            return "old man!"
        elif 18 <= self.__age < 65:
            return "you are adult!"
        else:
            return "young!"


yi = Student("yizhonglin", 28)
yang = Student("yangxc", 27)

# yi.print_age()
print(yang.get_age1())
# print(yang.age)
# print(yang.name)
print(yang.get_name(), ": ", yang.get_age())


