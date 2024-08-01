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
    print(counter.most_common(2))  # 输出最多的两个
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
    

# namedtuple的使用
# 在需要创建占用空间更少的不可变类时，命名元组就是很好的选择。
from collections import namedtuple

Card = namedtuple('Card', ('suite', 'face'))
card1 = Card('红桃', 13)
card2 = Card('草花', 5)
print(f'{card1.suite}{card1.face}')
print(f'{card2.suite}{card2.face}')


# 命名元组本质是一个类，所以可以作为父类创建子类。还有一些方法可以使用
# 比如_asdict方法将命名元组处理成字典，也可以通过_replace方法创建命名
# 元组对象的浅拷贝
class MyCard(Card):
    
    def show(self):
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{self.suite}{faces[self.face]}'


print(Card)    # <class '__main__.Card'>
card3 = MyCard('方块', 12)
print(card3.show())    # 方块Q
print(dict(card1._asdict()))    # {'suite': '红桃', 'face': 13}
print(card2._replace(suite='方块'))    # Card(suite='方块', face=5)