# 闭包中局部变量i的生命周期被延展，使得i的最终值3被最终参与计算

# 闭包是支持一等函数的编程语言（Python、JavaScript等）中实现词
# 法绑定的一种技术。当捕捉闭包的时候，它的自由变量（在函数外部定
# 义但在函数内部使用的变量）会在捕捉时被确定，这样即便脱离了捕捉
# 时的上下文，它也能照常运行。简单的说，可以将闭包理解为能够读取
# 其他函数内部变量的函数。正在情况下，函数的局部变量在函数调用结
# 束之后就结束了生命周期，但是闭包使得局部变量的生命周期得到了延
# 展。使用闭包的时候需要注意，闭包会使得函数中创建的对象不会被垃
# 圾回收，可能会导致很大的内存开销，所以闭包一定不能滥用。
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