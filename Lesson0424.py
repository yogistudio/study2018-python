"""
邮校学习
0424
模块对象
模块->语句->表达式
表达式有返回,语句无
"""


def testfun(a=[]):
    print(a)
    a.append(42)


testfun()
testfun(['hello'])
testfun()
testfun()
testfun()
testfun()

# []
# ['hello']
# [42]
# [42, 42]
# [42, 42, 42]
# [42, 42, 42, 42]
# 注意默认参数不要用可变的类型或者对象,这样会导致多次调用时参数值会发生变化

import sys  # 这个是build-in的

for i in sys.path:
    print(i)

# 在模块引用中,有个__name__,这个取值在本文件运行时为__main__,如果为其他引用文件中运行时,显示的为当前的文件名

# 包的概念,包含__init__.py的文件夹,所有全局对象都是包属性,包是一个模块对象,

# from amodule import btest
# from amodule.btest import *
# 只用第一种方法,不要用第二种,因为第二种中引用模块中的参数是不带模块名的,如被引用模块中有个aval,\
# 第二种方式引用中如果出现aval定义,会被冲掉,第一种方式如果用aval是需要前面带模块名的

# import只引用一次,为解决问题,加入 from imp import reload,加入这个后,对需要重载的引用在需要地方直接加 reload(模块名)

