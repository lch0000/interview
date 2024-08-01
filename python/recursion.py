from functools import lru_cache

# 找钱，多少种找零的方式，去重（下边的算法无去重）
@lru_cache
def change_money(total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total -2) + change_money(total - 3) + \
        change_money(total - 5)

print(change_money(7))

# 实现记忆缓存的装饰器
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i<2:
        return 1
    return fib(i-1) + fib(i-2)

print(fib(5))