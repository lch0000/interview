from concurrent.futures import ThreadPoolExecutor

# 创建Executor对象，指定线程池中线程数
executor = ThreadPoolExecutor(3)

def f(a, b):
    print('f', a, b)
    return a ** b

# 调用线程池中线程去执行函数
future = executor.submit(f, 2, 3)
# 使用线程池中一个线程运行这个函数，这个函数运营完之后又会归还

# 使用result得到函数的运行结果
print(future.result())
# 如果函数的运行时间比较长，在调用result的时候他还没有执行完，result会被阻塞直到函数运行完

# 在多个线程上同时调用f，类似于python的map方法
executor.map(f, [2,3,5], [4,5,6])

import time

def f2(a, b):
    print('f2', a, b)
    time.sleep(10)
    return a ** b

executor.map(f2, [2,3,5,6,7], [4,5,6,7,8])

# 使用with来管理好上下文
with ThreadPoolExecutor(max_workers=6) as executor:
    pass