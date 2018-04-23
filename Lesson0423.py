'''
邮校学习
0423
python可以在命令行直接执行 命令为 python -c "print 3*5",当中直接执行-c后面的语句
python -m pydoc -p 1234  在本机1234端口开通pyton文档的web
help(base64)
'''

print("hello ,world")


'''
Check if input-number > 42
'''
aStr = input("Input: ")
# print aStr
aInt = int(aStr)
if aInt > 42:
    print("> 42")
else:
    print("<= 42")
