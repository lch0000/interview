import random

# 生成[0.0, 1.0)之间的随机浮点数
print(random.random())

# 生成[a, b]或[b, a]之间的随机浮点数
print(random.uniform(1, 10))

# 生成[a, b]或[b, a]之间的随机整数
print(random.randint(1, 10))

# 实现对序列x的原地随机乱序
alist = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(alist)
print(alist)

# 从非空序列中取出一个随机元素
print(random.choice([1,2,3,4,5,6,7,8,9,10]))

# 从总体中随机抽取（有放回抽样）出容量为k的样本并返回样本的列表，可以通过参数指定个体的权重，如果没有指定权重，个体被选中的概率均等
print(random.choices([1,2,3,4,5,6,7,8,9,10], weights=None, cum_weights=None, k=8))

# 从总体中随机抽取（无放回抽样）出容量为k的样本并返回样本的列表
print(random.sample([1,2,3,4,5,6,7,8,9,10], k=8))

# random模块提供的函数除了生成均匀分布的随机数外，还可以生成其他分布
# 的随机数，例如random.gauss(mu, sigma)函数可以生成高斯分布（正态分
# 布）的随机数；random.paretovariate(alpha)函数会生成帕累托分布的随
# 机数；random.gammavariate(alpha, beta)函数会生成伽马分布的随机数