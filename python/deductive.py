# 推导式
items = [1, 2, 3, 4] 
print([i for i in items if i > 2])
print([i for i in items if i % 2])
print([(x, y) for x, y in zip('abcd', (1, 2, 3, 4, 5))])
print({x: f'item{x ** 2}' for x in (2, 4, 6)})
print(len({x for x in 'hello world' if x not in 'abcdefg'}))
print({x for x in 'hello world' if x not in 'abcdefg'})