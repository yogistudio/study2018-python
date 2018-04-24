"""
邮校学习
0424
异常处理
"""
# while True:
#     anumber = input('please input a number')
#     try:
#         afloat = int(anumber)
#         r = 10 / afloat
#     except ValueError as e:
#         print('ValueError', e)
#     except ZeroDivisionError as e:
#         print('Zero', e)
#     except Exception as e:
#         print(e)
#     else:
#         print('Result is % .3f' % r)
#     finally:
#         print('Finally')

# with or tyy

# with open('test.txt', 'r') as afile:
#     data = afile.read()

# 正则表达式
# ^ 开始,$ 结尾, ?前面一个元素出现零次或一次,
import re

reCmp = re.compile('\d{3,5}')  # a.+pl
if reCmp.search('http404'):
    print('Match')
else:
    print('Non-Match')

reCmp = re.compile('a.?pl', re.I)
print(reCmp.search('Appple'))

reCmp = re.compile(r'^(\d{0,3}\.){3}\d{0,3}$')
astr = '202.1.1.999'
if not reCmp.search(astr):
    print('error')
alist =[int(i) for i in astr.split('.')]

