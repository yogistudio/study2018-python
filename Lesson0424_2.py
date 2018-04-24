"""
邮校学习
0424
类对象
"""
import time
class Person(object):
    def __init__(self, name, birth):
        self.name = name
        self.brith = birth

    def greeting(self):
        print("Hi ,I'm ",self.name)

    def __str__(self):
        return '<Persion: %s> ' % self.name

    @property
    def age(self):
        return (time.time() - self.brith)/60/24/365


user1 = Person(name='User1', birth=0)
user2 = Person('User2', 10000)

user1.greeting()
user2.greeting()

print(str(user1))
print(user2)
print(user2.__str__())
print(user1.age)
print(user2.age)
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

print(Person.__base__)

# 类的继承是广度优先的

# super 调用父类的方法

# class Name(object):
#     def __init__(self, name):
#         self.name = name
#
#     def getLastName(self):
#         return self.name.split()[-1]
#
#     def __len__(self):
#         return len(self.name)
#
#     def split(self):
#         return  self.name.split()
#
#     def lower(self):
#         return self.name.lower()


class Name(str):
    def getLastName(self):
        return self.split()[-1]
# lower,len,split都在str中存在,所以可以直接继承str类,在实际应用中,最好用组合,就是第一种方式,不要用第二种继承

aName = Name("John Green")
print(aName.getLastName())
print(len(aName))
print(aName.split())
print(aName.lower())


# 反射代码,书中的这个需要看看

# Code:
class Queue(list):
    def push(self, i):
        self.append(i)

    def pull(self):
        return self.pop(0)


# 客户端代码/Run：
aQueue = Queue()
aQueue.push("hello")
aQueue.push(42)
print(len(aQueue))
print(aQueue.pull()) # hello
print(aQueue.pull()) # 42
print(aQueue.pull()) # IndexError

