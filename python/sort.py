import bisect

# sort方法，原地排序，默认升序
a = [7, 2, 5, 1, 3]
a.sort()
print(a)

# sorted函数，排序并返回值，reverse为真时降序
b = sorted(a, reverse=True)
print(b)

# bisect模块不会判断原列表是否有序
c = [1,2,2,2,3,4,7]
bisect.bisect(c, 2)
bisect.bisect(c, 5)

bisect.insort(c, 6)


prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

print(sorted(prices, key=lambda x: prices[x], reverse=True))