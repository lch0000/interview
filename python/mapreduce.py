from functools import reduce
from operator import add, sub, mul, imod
from random import randint, choice

# 实现叠加
print(reduce(add, [1,2,3,4]))
# 实现阶乘的计算
print(list(map(lambda x:reduce(mul, range(1,x+1)), [1,2,3,4])))
# 过滤器
print(list(filter(lambda x:x%2==0, [1,2,3,4])))
# lambda（匿名函数，为函数做解耦）
# 一行代码实现求阶乘（包含import）
fac = lambda x: __import__('functools').reduce(int.__mul__, range(1, x+1), 1)
# 一行代码实现求最大公约数（迭代）
gcd = lambda x, y: y % x and gcd(y %x, x) or x
#  从列表中筛选出奇数并求平方构成新列表
items = [12, 5, 7, 10, 8, 19]
items = list(map(lambda x: x**2, filter(lambda x: x % 2, items)))
print(items)
# 列表生成式
items = [x**2 for x in items if x%2]
print(items)