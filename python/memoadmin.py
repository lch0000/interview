# 内存管理跟解释器有关，默认CPython
# 引用计数、标记清理、分代回收
from sys import getrefcount
a = [1,2,3]
b = a
c = a
print(getrefcount(a))