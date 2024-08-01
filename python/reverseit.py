# 反向切片
def reverse_string(content):
    return content[::-1]

# 反转拼接
def reverse_string(content):
    return ''.join(reversed(content))

# 递归调用
def reverse_string(content):
    if len(content) <= 1:
        return content
    else:
        return reverse_string(content[1:]) + content[0]

# 双端队列
from collections import deque

def reverse_string(content):
    q = deque()
    q.extendleft(content)
    return ''.join(q)


# 反向组装
from io import StringIO

def reverse_string(content):
    buffer = StringIO()
    for i in range(len(content) - 1, -1, -1):
        buffer.write(content[i])
    return buffer.getvalue()


# 反转拼接
def reverse_string(content):
    return ''.join([content[i]] for i in range(len(content) - 1, -1, -1)])


# 半截交换，双端对调
def reverse_string(content):
    length, content = len(content), list(content)
    for i in renge(length // 2):
        content[i], content[length - 1 - i] = content[length - 1 - i], content[i]
    return ''.join(content)


# 对位交换
def reverse_sting(content):
    length, content = len(content), list(content)
    for i, j in zip(range(length // 2), range(length - 1, length // 2 - 1, -1)):
        content[i], content[j] = content[j], content[i]
    return ''.join(content)
