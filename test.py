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