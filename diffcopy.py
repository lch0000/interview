from copy import copy, deepcopy
innercont = [1,2, ['abc', 'mmm', 2], '']
outercont = [3,4,5]
outercont.append(innercont)
slicecont = outercont[:]
copycont = copy(outercont)
deepcopycont = deepcopy(outercont)
innercont[2][0] = 'xxx'
outercont[0] = 6
print(outercont)
print(slicecont)
print(copycont)
print(deepcopycont)

# 使用序列化和反序列化实现deepcopy
import pickle
my_deep_copy = lambda obj: pickle.loads(pickle.dumps(obj))

# 使用元类来实现原型模式
class PrototypeMeta(type):
    '''实现原型模式的元类'''

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为对象绑定clone方法来实现对象拷贝
        cls.clone = lambda self, is_deep=True: \
            deepcopy(self) if is_deep else copy(self)


class Person(metaclass=PrototypeMeta):
    pass


p1 = Person()
p2 = p1.clone()  # 深拷贝
p3 = p1.clone()  # 浅拷贝