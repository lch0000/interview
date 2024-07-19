# iterator
class Fib(object):

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0,1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()

f = Fib(10)
for x in f:
    print(x)

# generator
def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
        yield a

for x in fib(10):
    print(x)