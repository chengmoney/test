print('hello world')
a = 3
b = 4
c = a + b
print("c =", c)

# 定义函数
"""
def 函数名(函数1, 函数2, 函数3)
    函数本体  # 必须缩进4个空格
    
"""


def add_function(a, b):
    c = a + b
    print(c)


add_function(2, 3)


# 字符串
print("What's you name?")  # "and'可以嵌套
print('what\'s you name?')  # \表示转义符号，\后面的符号失去原有在python中的含义
print('"小明说自己是猪"')
print("\"小明说自己是猪\"")

# 变量可以储存字符串 type()函数可以查出变量的类型

text = '小明'
type(text)  # type(text) <class 'str'>

num = 8
type(num)   # type(num) <class 'int'>

num1 = 8.0
type(num1)  # type(num1) <class 'float'>

# 字符串的连接 用+号连接
a = 'Python'
b = '很NB'
c = a + b
print(c)

# \x表示转义 1.(在行尾时)续行符 2.\' 单引号  3.\" 双引号 4.\n 换行 5.\r 回车
print('请登录以下网址 http：//www.hao123.com')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
     hahahhah')
print('send QQ\\email\\weixin to me')
print('you are a SB \n SB')
print('you are a sb \r sb')  # \n 和\r 的区别 \n 表示换行  \r 只回到行首而仍在当前行
'''
print('you are a SB \n SB')
you are a SB 
 SB
print('you are a sb \r sb')
 sb
'''
# 字符串的格式化 %d 表示数字 %s 表示字符串

print('%s今年%d岁' % ('小王', 30))
name = '小王'
age = 30
print('%s今年%d岁' % (name, age))

text = input()
le = len(text)
print('%s有%d个字母' % (text, le))

# S.upper() #S中的字母大写
# S.lower() #S中的字母小写
# S.capitalize() #首字母大写

s = 'small'
print(s.upper())
print(s)  # 不改变原有变量

b = s.upper()
print(b.lower())
print(b)  # 不改变原有变量

print(s.capitalize())
print(s.title())

# capitalize() and title() 的区别
s = 'you are a sb'
print(s.capitalize())
print(s.title())  # capitalize()是对该字符串的第一个字母操作 # title()是对该字符串中的所有单词的首字母操作
'''
    You are a sb
    You Are A Sb
'''

# S.istitle() #单词首字母是否大写的，且其它为小写
# S.isupper() #S中的字母是否全是大写
# S.islower() #S中的字母是否全是小写




