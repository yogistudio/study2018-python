"""
变量是一个引用,可以指向任何对象
变量必须先赋值,才能被使用
zip返回的是生成器,只能用一次
只有一行的时候,for语句可以没有下面的缩进
for i in rang(2):
    pass
for in in range(2): pass
x,y =1,2
y,x = x,y
alist= [1,2,3]
alist.append(1)
del alist[2:3]  删除的时候也可以使用切片
如果一个对象没有被引用,不是马上删除,看pvm的调用,如果有引用,或者是某个变量的一部分,也不会删除的
如果有自引用,但是前被删除,后面还有一个能够引用自身,本身有引用,但是实际是孤岛,
PVM的垃圾回收机制是根据是否是孤岛(有没有变量指向),而不是看有没有引用

变量名规则,不能以数字开头,
astr='12 34 56'
blist = [int(i)**2 for i in astr.split()]
cgi每个请求对应一个进程,fastcgi定义多个,不会每次启用
mvc,mtc(django),T视图,C控制
legb,l本地,E,上一程,G,全局,B,内置
"""
atuple = (1, 2)
aset = set("hello")

adict = {'a': 2}
alist = [1, 2]
alist.append(4)
blist = [3, 4]
blist.append(6)
alist[1:2] = ["test", "test1", "test2", "test3"]  # 实际增加的时候,是不管切片的,都加进去了
clist = list(zip(alist, blist))
print(clist)  # 如果使用一次,第二次就没有了
print(clist)
print(alist)
bdict = dict(clist)
print(bdict)
bdict["a"] = 3
del bdict[1]
print(bdict)
print(bdict.get('apple2', 'Noee'))

astr = '12 34 56'
elist = [int(i) ** 2 for i in astr.split()]
flist = ''.join(str(i) for i in elist)
print(int)
print(elist)
print(flist)
huiwei = lambda x: x == x[::-1]
glist = ['bob', 'hello', 'haha', 'abba']
hlist = [i for i in glist if i == i[::-1]]
print(hlist)
llist = [i for i in glist if i is huiwei(i)]
print(hlist)
mlist = filter(huiwei, glist)
nlist = map(huiwei, glist)
print(list(mlist), list(nlist))


def isequeal(afloat, bfloat):
    n = 10 ** -10
    return abs(afloat - bfloat) < n


bstr = ["hello", "test", "a", "hashable"]
cstr = [i for i in sorted(bstr, key=len)]
dstr = [i for i in sorted(bstr, key=len, reverse=True)]
print(cstr, dstr)

from collections import Counter

astr = 'aaaaaaabbbbccc'
alist = Counter(astr)
blist = [astr.count(i) for i in set(astr)]
print(alist, blist)

adict = {"a": 2, "b": 3}
alist = ["%s=>%s" % (k, v) for k, v in adict.i]
",".join(alist)
print(alist)

def fib():
    a,b=1,2
    while True:
        yield  a
        a,b=b,a+b
import time
for i in fib():
    print(i)
    time.sleep(1)

