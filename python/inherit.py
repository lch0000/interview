# 继承的引用关系
class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

'''
1、Python中的MRO（方法解析顺序）。在没有多重继承的情况下，向对象发出一
个消息，如果对象没有对应的方法，那么向上（父类）搜索的顺序是非常清晰
的。如果向上追溯到object类（所有类的父类）都没有找到对应的方法，那么
将会引发AttributeError异常。但是有多重继承尤其是出现菱形继承（钻石继
承）的时候，向上追溯到底应该找到那个方法就得确定MRO。Python 3中的类
以及Python 2中的新式类使用C3算法来确定MRO，它是一种类似于广度优先搜
索的方法；Python 2中的旧式类（经典类）使用深度优先搜索来确定MRO。在
搞不清楚MRO的情况下，可以使用类的mro方法或__mro__属性来获得类的MRO列表。

2、super()函数的使用。在使用super函数时，可以通过super(类型, 对象)来指
定对哪个对象以哪个类为起点向上搜索父类方法。所以上面B类代码中的
super(B, self).who()表示以B类为起点，向上搜索self（D类对象）的
who方法，所以会找到C类中的who方法，因为D类对象的MRO列表是
D --> B --> C --> A --> object。
'''
class A:
    def who(self):
        print('A', end='')

class B(A):
    def who(self):
        super(B, self).who()
        print('B', end='')

class C(A):
    def who(self):
        super(C, self).who()
        print('C', end='')

class D(B, C):
    def who(self):
        super(D, self).who()
        print('D', end='')

item = D()
item.who()
print()
