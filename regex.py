import re
# python中默认是贪婪匹配
regex = r'a.*d'  # 匹配abcdabcd
regex_mini = r'a.*?d'  # 匹配abcd
match = re.match(regex, 'abcdabcd')
match_mini = re.match(regex_mini, 'abcdabcd')
match.group()
match_mini.group()
print(match)
print(match_mini)

# match和search的区别
# match默认匹配头部，可以加入偏移
# search在整段字符串中进行搜索
# sub用于检索和替换
phone = '2004-959-559 # 这是一个国外的电话号码'
# 删除字符串中的python注释
num = re.sub(r'#.*$', '', phone)
print('电话号码是：', num)

# 删除非数字（-）的字符串
num = re.sub(r'\D', '', phone)
print('电话号码是：', num)

# 通过repl将匹配的字符串中的数字翻倍
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A55G8HDD337'
print(re.sub('(?P<value>\d+)', double, s))

# findall找到字符串中正则匹配的所有子串，并返回一个列表，如果有多个匹配模式则返回元组
result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)
# finditer类似findall，返回迭代器
it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())

# re.split能按照匹配的字符串将字符串分割后返回列表

# 匹配身份证并返回匹配字典
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())