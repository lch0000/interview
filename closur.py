# 闭包中局部变量i的生命周期被延展，使得i的最终值3被最终参与计算
print([m(100) for m in [lambda x: i*x for i in range(4)]])

def multiply():
    return [lambda x: i*x for i in range(4)]

print([m(100) for m in multiply()])

def multiply():
    return (lambda x: i*x for i in range(4))

print([m(100) for m in multiply()])

def multiply():
    for i in range(4):
        yield lambda x: x*i

print([m(100) for m in multiply()])

# 使用偏函数，彻底避开闭包
from functools import partial
from operator import __mul__

def multiply():
    return [partial(__mul__, i) for i in range(4)]

print([m(100) for m in multiply()])

# 偏函数实例
# 在计算机科学中，偏函数是固定一个函数的一些参数，然后生成一个新的函数的行为
def multiply(x, y):
    return x * y

double = partial(multiply, y=2)
print(double(3))