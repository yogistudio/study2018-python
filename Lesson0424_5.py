"""
邮校学习
0424
生成器和迭代器
"""
alist = range(3)
for i in alist:
    print(i)

# 实际可以解析为
aiter = iter(alist)
while True:
    try:
        i = aiter.__next__()
    except StopIteration:
        break
    print(i)


# 对于一个迭代器,再次迭代,返回的是自身

def genSeq():
    yield 1
    yield 2
    yield 3
    yield 'hello'
    yield 10


agen = genSeq()
# 函数定义时会代码全部执行,但是生成器(有yield)不会执行任何代码,执行时最后返回StopIteration
# print(agen.__next__())
# print(agen.__next__())
# print(agen.__next__())
# print(agen.__next__())
# print(agen.__next__())
# print(agen.__next__())

for i in agen:
    print(i)


# 应用场景,斐波立即数列
def fib(n):
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(fib(i))

    # print(fib(40))

import time


#
# a, b = 1, 2
# while True:
#     print(a)
#     a, b = b, b + a
#     time.sleep(1)

# def Fib():
#     a, b = 1, 2
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for i in Fib():
#     print(i)
#     time.sleep(1)
