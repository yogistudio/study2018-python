'''
邮校学习
0423
python可以在命令行直接执行 命令为 python -c "print 3*5",当中直接执行-c后面的语句
python -m pydoc -p 1234  在本机1234端口开通pyton文档的web
help(base64)
'''
import random

# '''
# Check if input-number > 42 输入一个数字,判断是否大于42
# '''
# aStr = input("Input: ")
# # print aStr
# aInt = int(aStr)
# if aInt > 42:
#     print("> 42")
# else:
#     print("<= 42")

# inputstr = input('Please input a number:')
# inputnumber = int(inputstr)
# if inputnumber >= 42:
#     print('you number is ' + inputstr + ' is over or equal 42')
# else:
#     print('you number is ' + inputstr + ' is bless  42')

#猜大小,给定一个数字1-100,6次机会猜数字
# judgenum = random.randint(1, 100)
# print('this is a game for guess a number,you have 6 chance')
# for i in range(6):
#     inputjudge = int(input('Please input a number:'))
#     if inputjudge > judgenum:
#         print('You number is Over!')
#     elif inputjudge == judgenum:
#         print('Great, You are right!')
#         break
#     else:
#         if i != 5:
#             print('You number is bless!')
#         else:
#             print('You lose this game! number is %d' % judgenum)

#int变换进制
# print(int("12"))
# print(int('12', 8))
# print(int('12', 16))

#浮点值的比较不能直接用==,使用abs(2.3+2.4-4.7)<N,定义N为一个很小的值,如,N=0.000001
# Tip_020103 随机生成两个10以内的实数（小数点后两位）并输出到屏幕，要求输入他们的和，输出True/False。

# Run:
# Please input sum for 4.96 + 4.91 =
# 9.87
# Right!
#
# Code:
from random import random
#定义一个常量非常小的数字,**乘方,开根号 2开2次方 2**(1/2)
#help(random.random)得到的值为[0,),[0表示可以取到0,1)表示取不到1
# MIN_DELTA = 10 ** -10
#
#
# aFloat = round(random() * 10, 2)
# bFloat = round(random() * 10, 2)
# sumStr = input("Please input sum for %.2f + %.2f =\n" % (aFloat, bFloat))
# if abs(float(sumStr) - (aFloat+bFloat)) < MIN_DELTA:#float的取值比较不能用==的举例
#     print("Right!")
# else:
#     print("Wrong!")

#输入2个数字,得到和
'''
d,i                 带符号的十进制整数
o                   不带符号的八进制
u                   不带符号的十进制
x                    不带符号的十六进制（小写）
X                   不带符号的十六进制（大写）
e                   科学计数法表示的浮点数（小写）
E                   科学计数法表示的浮点数（大写）
f,F                 十进制浮点数
g                   如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
G                  如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
C                  单字符（接受整数或者单字符字符串）
r                    字符串（使用repr转换任意python对象)
s                   字符串（使用str转换任意python对象）
'''
# aStr = input('Int A = ')
# bStr = input('Int B = ')
# aInt = int(aStr)
# bInt = int(bStr)
# print("%s + %s = %s" % (aInt, bInt, aInt+bInt))

#字符串单引号和双引号都是一样的,可以用于转义,如 print('you are "hello"') 或者 print("you's")

astr = '0123456789'

#单冒号
# print(astr[3:6])
# #左闭右开
# print(astr[3:])
# print(astr[3:None])
# #双冒号,表示步长
# print(astr[2::2])
# print(astr[::2])
print(astr[2:8:2])
print(astr[7:1:-2])#取值-2表示从第一个即7开始,2:8:2,表示从2开始到8,从左到右,2:8:-2

# bstr='apple pear banana'
# cstr = bstr[::-1].split()[::-1]
# print(cstr)

#python对不可变对象只存储一份,如下文,元组中的0,2都是取值0,所以他们对象的地址是一致的

# a=(0,'a',0,1)
# print(id(a[0]))
# print(id(a[2]))
'''
列表解析[i(表达式) for i in range(10)(取值) if i % 3 == 0(判断条件)]
for i in range(1,6)
print(i**2)
i**2 是表达式,for i in range(1,6)为取值,判断条件可以省略
'''

aList = [i for i in range(10) if i % 3 == 0]
print(aList)

alist = [[0]]*3
#[[0],[0],[0]]
alist[0][0] = 'hello'
# alist=[[0]]*3
# [[0], [0], [0]]
# [id(i) for i in alist]
# [52273480, 52273480, 52273480]
# [['hello'],['hello'],['hello']]

# blist=[0]
# alist = [blist for i in range(3)]
# alist
# [[0], [0], [0]]
# blist = ['hello']
# blist
# ['hello']
# alist
# [[0], [0], [0]]
#
# alist
# [[0], [1], [3]]
# blist
# [[0], [1], [3]]
# alist[2]='hello'
# id(alist),id(blist)
# (52783816, 52783816)
# alist,blist
# ([[0], [1], 'hello'], [[0], [1], 'hello'])
# import copy
# alist=[[0],[1],[2]]
# blist=alist
# blist=copy.copy(alist)
# clist=alist
# alist,blist,clist
# ([[0], [1], [2]], [[0], [1], [2]], [[0], [1], [2]])
# alist[0]='hello'
# alist,blist,clist
# (['hello', [1], [2]], [[0], [1], [2]], ['hello', [1], [2]])
# dlist=copy.deepcopy(alist)
# alist,blist,clist,dlist
# (['hello', [1], [2]], [[0], [1], [2]], ['hello', [1], [2]], ['hello', [1], [2]])
# alist[2][0]='xixi'
# alist,blist,clist,dlist
# (['hello', [1], ['xixi']], [[0], [1], ['xixi']], ['hello', [1], ['xixi']], ['hello', [1], [2]])

# elist=alist[:]
# elist=alist+[]
# elist=alist*1
#以上3中方式均为全拷贝 copy全拷贝,deepcopy 深拷贝
#alist = alist+[0] ,id(alist)变, alist+=[0] ,id(alist)不变

