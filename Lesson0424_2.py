"""
邮校学习
0424
类对象
"""
class Person(object):
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hi ,I'm ",self.name)
    def __str__(self):
        return '<Persion: %s> ' % self.name

user1 = Person(name = 'User1')
user2 = Person(name = 'User2')

user1.greeting()
user2.greeting()

print(str(user1))
print(user2)
print(user2.__str__())

# __solt__用来绑定属性,但是仅对当前层次,不约束子类

class AddN(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, x):  # __call__是重载类的括号运算符
        return x+self.n

add3 = AddN(3)
add4 = AddN(4)
print(add3(40))
print(add4(40))

# def addN(n):
#     def add(x):
#         return x+n
#     return add
# add3 = addN(3)#3是n
# add4 = addN(4)#4是n
#
# print(add3(42))#42是x
# print(add4(25))#25是x
# 这个函数实现的与上面类实现的相同.但是类可以修改n的取值