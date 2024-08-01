# 要求：写一个函数，传入一个有若干个整数的列表，该列表中
# 某个元素出现的次数超过了50%，返回这个元素。
def more_than_half(items):
    temp, times = None, 0
    for item in items:
        if times == 0:
            temp = item
            times += 1
        else:
            if item == temp:
                times += 1
            else:
                times -= 1
    return temp

# 要求：写一个函数，传入的参数是一个列表（列表中的元素可能
# 也是一个列表），返回该列表最大的嵌套深度。例如：列表[1, 2, 3]
# 的嵌套深度为1，列表[[1], [2, [3]]]的嵌套深度为3。
def list_depth(items):
    if isinstance(items, list):
        max_depth = 1 # 需要有一个变量存储之前得到的最大深度
        for item in items:
            max_depth = max(list_depth(item) + 1, max_depth)
        return max_depth
    return 0


# 要求：列表中有1000000个元素，取值范围是[1000, 10000)，设计
# 一个函数找出列表中的重复元素。
def find_dup(items: list):
    dups = [0] * 9000
    for item in items:
        dups[item - 1000] += 1
    for idx, val in enumerate(dups):
        if val > 1:
            yield idx + 1000

# [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
def pairs(n):
    return [list(x) for x in zip(range(1,n+1), range(1,n+1))]

def pairs(n):
    if n > 0:
        return pairs(n-1)+[[n,n]]
    else:
        return []