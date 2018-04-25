"""
邮校学习
0424
装饰器
多个装饰器,越近的越先处理,用于框架中间层
"""


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold  # 等价于 hello = makebold(hello)
@makeitalic
def hello():
    return "hello world"


print(hello())
