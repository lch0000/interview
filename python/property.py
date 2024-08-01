class A: 
    # __slots__ = ('__value',)
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

obj = A(1)
obj.__value = 2
obj.__test = 3
print(obj.value)
print(obj.__value)
print(obj.__dict__)
# {'_A__value': 1, '__value': 2, '__test': 3}
# 在记录时类中的私有数据被添加前缀_classname