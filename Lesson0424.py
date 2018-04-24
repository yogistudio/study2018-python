"""
邮校学习
0424
模块对象
模块->语句->表达式
表达式有返回,语句无
"""


# def testfun(a=[]):
#     print(a)
#     a.append(42)
#
#
# testfun()
# testfun(['hello'])
# testfun()
# testfun()
# testfun()
# testfun()

# []
# ['hello']
# [42]
# [42, 42]
# [42, 42, 42]
# [42, 42, 42, 42]
# 注意默认参数不要用可变的类型或者对象,这样会导致多次调用时参数值会发生变化

# import sys  # 这个是build-in的
#
# for i in sys.path:
#     print(i)

# 在模块引用中,有个__name__,这个取值在本文件运行时为__main__,如果为其他引用文件中运行时,显示的为当前的文件名

# 包的概念,包含__init__.py的文件夹,所有全局对象都是包属性,包是一个模块对象,

# from amodule import btest
# from amodule.btest import *
# 只用第一种方法,不要用第二种,因为第二种中引用模块中的参数是不带模块名的,如被引用模块中有个aval,\
# 第二种方式引用中如果出现aval定义,会被冲掉,第一种方式如果用aval是需要前面带模块名的

# import只引用一次,为解决问题,加入 from imp import reload,加入这个后,对需要重载的引用在需要地方直接加 reload(模块名)

# 类和类的实例化,存储模型,定义,引用,继承

class TestClass(object):
    """
    测试类
    """
    value_a = 'test'
    value_b = list(range(3))
    value_c = 'modify'
    def testMethod(self):
        print('Test Method')
    def returnValuec(self):
        print(self.value_c)
    @property
    def propertyMethon(self):
        print(self.value_a + self.value_c)

testclass = TestClass()
test2class = TestClass()
print(TestClass.__name__)
print(TestClass.__doc__)
print(TestClass.__dict__)
print(TestClass.__base__)

for i,j in TestClass.__dict__.items():
    print(i, j)

print(testclass)
print(testclass.__class__)  # 实例化是直接通过此属性指向类
print(id(testclass.__class__),id(TestClass))  # 37919384 37919384,可以看到指向地址一致

test2class.value_a = 'New'
print(testclass.value_a)  # 定义一个新映射不改变原值,只是相当于新建一个dict键对
test2class.value_b[2] = 'new'  # 这样定义的时候,不是value_b定义映射,只是用于索引,所以这样修改的是TestClass的本身内存内容,这样就会影响本身及所有实例.
# 所以不要在类中定义可变属性,因为这会导致不可知的问题
print(testclass.value_b)
test2class.newvalue = 'test'
# print(testclass.newvalue)  c此语句会报错,因为这个引用不会有这个值

TestClass.value_c = 'modify test'
print(test2class.value_c, TestClass.value_c)  # 如果类定义直接修改,那么修改的是内存内容,所有实例均会修改


test2class.returnValuec()  #  等于 TestClass.returnValuec(test2class)
test2class.value_c = 'new 3'
test2class.returnValuec()  # 这样修改后用的是本地实例的valuec,这样返回的就是新值

print('prot')
test2class.propertyMethon  # property定义中是函数,访问的时候直接不加括号,与属性访问相同

# property看上去像属性,实际上是一个方法
