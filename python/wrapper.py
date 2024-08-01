# 闭包是支持一等函数的编程语言（Python、JavaScript等）中实现词
# 法绑定的一种技术。当捕捉闭包的时候，它的自由变量（在函数外部定
# 义但在函数内部使用的变量）会在捕捉时被确定，这样即便脱离了捕捉
# 时的上下文，它也能照常运行。简单的说，可以将闭包理解为能够读取
# 其他函数内部变量的函数。正在情况下，函数的局部变量在函数调用结
# 束之后就结束了生命周期，但是闭包使得局部变量的生命周期得到了延
# 展。使用闭包的时候需要注意，闭包会使得函数中创建的对象不会被垃
# 圾回收，可能会导致很大的内存开销，所以闭包一定不能滥用。
from functools import wraps
from random import random
from textwrap import wrap
from time import time, sleep

def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}执行时间：{time() - start}秒')
        return result
    
    return wrapper

@record_time
def sleep2():
    sleep(2)

print(sleep2())

# 用类实现装饰器
class Record:
    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            print(f'{func.__name__}执行时间：{time() - start}秒')
            return result

        return wrapper

# 注意这里的调用方法
@Record()
def sleep3():
    sleep(3)

print(sleep3())

# 带参数的装饰器,在最外层带上参数
def record_time_para(output):
    '''可以参数化的装饰器'''

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper

    return decorate
    
# 要求：有一个通过网络获取数据的函数（可能会因为网络原因出现异常），
# 写一个装饰器让这个函数在出现指定异常时可以重试指定的次数，并在每
# 次重试之前随机延迟一段时间，最长延迟时间可以通过参数进行控制。
def retry(*args, retry_times=3, max_wait_secs=5, errors=(Exception, )):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retry_times):
                try:
                    return func(*args, **kwargs)
                except errors:
                    sleep(random() * max_wait_secs)
            return None
        return wrapper
    return decorate

class Retry(object):
    def __init__(self, *, retry_time=3, max_wait_secs=5, errors=(Exception, )):
        self.retry_times = retry_times
        self.max_wait_secs = max_wait_secs
        self.errors = errors

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.retry_times):
                try:
                    return func(*args, **kwargs)
                except self.errors:
                    sleep(random() * self.max_wait_secs)
            return None
        return wrapper