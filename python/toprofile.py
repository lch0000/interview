import cProfile
import hashlib
import profile

def is_prime(num):
    '''判断素数'''
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True

class PrimeIter:

    def __init__(self, total):
        self.counter = 0
        self.current = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.total:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
            self.counter += 1
            return self.current
        raise StopIteration()


cProfile.run('list(PrimeIter(100))')

# 在ipython中可以使用如下方式 %timeit for _ in range(1000): True

# 使用line_profiler, 命令行下执行kernprof -lv example.py

@profile
def set_md5(char_val):
    '''md5加密'''
    if not isinstance(char_val, bytes):
        char_val = char_val.encode('utf-8')
    m = hashlib.md5()
    m.update(char_val)
    return m.hexdigest()