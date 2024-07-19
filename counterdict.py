# 统计列表中每个数字出现的次数并返回对应字典
def count_letters(items):
    result = {}
    for itme in items:
        if isinstance(item, (int, float)):
            result[item] = result.get(item, 0) + 1
    return result

# 使用标准库中collections的Counter类来处理
from collections import Counter

def count_letters(items):
    counter = Counter(items)
    print(counter)
    print(dict(counter))
    return {key: value for key, value in counter.items() \
            if isinstance(key, (int, float))}

count_letters([1,1,2,2,2,3,'abc'])

# defaultdict的使用
from collections import defaultdict
bag = ['apple', 'orange', 'cherry', 'apple', 'apple', 'cherry', 'blueberry']
count = defaultdict(int)
for fruit in bag:
    # count.setdefault(fruit, 0)
    count[fruit] += 1
    