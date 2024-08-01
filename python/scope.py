'''
python中有四种作用域
L（Local）局部作用域
E（Enclosing）闭包函数外的函数中
G（Global）全局作用域
B（Built-in)内建作用域
L->E->G->B
'''

# dir为python内建函数
dir = 1
def outer():
    dir = 2
    def inner():
        dir = 3
        return dir
    return inner

print(outer()())