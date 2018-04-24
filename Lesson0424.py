"""
邮校学习
0424
模块对象
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

