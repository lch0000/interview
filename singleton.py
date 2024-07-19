from functools import wraps

# 装饰器方法实现
def singleton(cls):
    '''单例装饰器'''
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrapper

@singleton
class President(object):
    pass



# 元类方法实现
class SingletonMeta(type):
    '''自定义单例元类'''
    def __init__(cls, *args, **kwargs):
         cls.__instance = None
         super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President2(metaclass=SingletonMeta):
    pass


# __new__方法实现
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            orig = super(Singleton, cls)
            cls.__instance = orig.__new__(cls, *args, **kwargs)
        return cls.__instance

class President3(Singleton):
    pass

if __name__ == "__main__":
    test_class = President()
    test_class.x = 'x is in President'
    new_class = President()
    print(new_class.x)