# 用栈实现逆波兰表达式
import operator

class Stack:
    '''栈（FIFO）'''

    def __init__(self):
        self.elems = []

    def push(self, elem):
        '''入栈'''
        self.elems.append(elem)

    def pop(self):
        '''出栈'''
        return self.elems.pop()

    @property
    def is_empty(self):
        '''检查栈是否为空'''
        return len(self.elems) == 0


def eval_suffix(expr):
    '''
    逆波兰表达式求值
    逆波兰表达式也称为“后缀表达式”，相较于平常我们使用的“中缀表达式”，
    逆波兰表达式不需要括号来确定运算的优先级，例如5 * (2 + 3)对应的逆
    波兰表达式是5 2 3 + *。逆波兰表达式求值需要借助栈结构，扫描表达式
    遇到运算数就入栈，遇到运算符就出栈两个元素做运算，将运算结果入栈。
    表达式扫描结束后，栈中只有一个数，这个数就是最终的运算结果，直接出
    栈即可。
    '''
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    stack = Stack()
    print(expr.split())
    for item in expr.split():
        if item.isdigit():
            stack.push(float(item))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.push(operators[item](num1, num2))
    return stack.pop()

print(eval_suffix('5 2 3 + *'))