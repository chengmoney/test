# 在python中，用方括号表示一个list，[ ]
a = []  # 定义一个变量a，数据类型为list，内容为空
type(a)
bool(a)  # 看看list类型的变量a的布尔值，因为是空的，所以为False

a = ['abc', 34, '成驭']
print(a)

# list索引
ur = ['ab', 34, 'chengyu']
print(ur[0])  # 索引序号也是从0开始
print(a[:2])  # 列出 'ab', 34

# list追加元素  Add an item to the end of the list; equivalent to a[len(a):] = [x].
a = ['abc', 34, '成驭']
a.append(45)  # 向a list中添加45
a  # ['abc', 34, '成驭', 45]

# 另外一种追加list的方法  a[len(a):] = [x]
a = ['abc', 34, '成驭']
len(a)  # 长度为3
a[len(a):] = ['ab', 35]

# 合并list  list.extend(L) Extend the list by appending all the items in the given list;
la = [1, 3, 56]
lb = ['a', 'b', 'abc']
la.extend(lb)
print(la)

text = 'avc'
num = 5
la.extend(text)
print(la)  # [1, 3, 56, 'a', 'b', 'abc', 'a', 'v', 'c']  text以字符为单位拆开添加进入la中
la.extend(num)  # 不能添加数字，会报错  TypeError: 'int' object is not iterable

# 试一试添加汉字
lb = [1, 3, 5]
text = '我是成'
lb.extend(text)
print(lb)  # [1, 3, 5, '我', '是', '成']

# list.extend and list.append 的区别  append是成建制的追加，extend是个体化扩编
la = [1, 2, 3]
lb = [4, 5]
la.append(lb)  # [1, 2, 3, [4, 5]]

la = [1, 2, 3]
lb = [4, 5]
la.extend(lb)
print(la)  # [1, 2, 3, 4, 5]

la = [1, 2, 3]
lb = [4, 5]
la[len(la):] = [4, 5]
print(la)  # [1, 2, 3, 4, 5]

la = [1, 2, 3]
lb = [4, 5]
la[len(la):len(la) + 1] = [4, 5]
print(la)  # [1, 2, 3, 4, 5]

la = []
text = '0123456789'
la.append(text)  # ['0123456789']

la = []
text = '123456789'
la.extend(text)
print(la)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(la[1:3])  # 从0开始编码，截取la的2-3位。用la[a:b] a表示从哪一位开始，
# b表示从哪一位截止，截止的位数不包含b位

# list 中某元素个个数 list.count(x) 返回值是一个数字
lt = [1, 1, 1, 3, 4, '1']
a = lt.count(1)
b = lt.count(2)
c = lt.count(3)
d = lt.count('1')
type(a)  # <class 'int'>
print(a, b, c, d)  # 3 0 1 1

# 元素在list中的位置 list.index()
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.

lt = [1, 2, 3, 4, 1, 5]
a = lt.index(1)
type(a)  # <class 'int'> 返回值是int
print(a)  # 0  list中第一次出现1的元素位置
b = lt.index(3)
print(b)  # 2
c = lt.index(6)  # ValueError: 6 is not in list 报错

# 向list中插入一个元素（指定位置插入） list.insert(i, x)
# Insert an item at a given position. The first argument(参数） is the index of the element before which to insert
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

lt = ['a', 'b', 'c', 'd']
lt.insert(0, 'aa')  # 在list第一个元素前插入一个元素
lt.insert(2, 'a')  # 在list第3个元素前插入一个元素
lt.insert(len(lt), 'a')  # 在list最后追加一个元素
lt.insert(len(lt), ['ab', 'ac'])  # ==lt.append(['ab', 'ac']
print(lt)  # ['aa', 'a', 'a', 'b', 'c', 'd', 'a', ['ab', 'ac']]

# list的删除  list.remove(x)
# Remove the first item from the list whose value is x. It is an error if there is no such item
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and
# returns the last item in the list.
lt = ['aa', 'a', 'a', 'b', 'c', 'd', 'a']
lt.remove('a')  # 删除了list中第一个内容是'a'的值。不会删除所有的内容是'a'的值
print(lt)  # ['aa', 'a', 'b', 'c', 'd', 'a']
lt.remove("1")  # ValueError: list.remove(x): x not in list

lt = ['aa', 'a', 'a', 'b', 'c', 'd', 'a']
c = lt.pop(3)  # 删除list中第4个元素，且将删除的'b'储存在c变量中
print(c)
print(lt)

# 实验list.remove()有没有返回值
lt = ['aa', 'a', 'a', 'b', 'c', 'd', 'a']
d = lt.remove('a')
print(d)  # None  不产生返回值

#   判断一个元素在不在list中用 a in list
lt = ['aa', 'a', 'a', 'b', 'c', 'd', 'a']
lt.append(['a', 'a'])
print('a' in lt)  # 产生一个返回值true
print(['a', 'a'] in lt)  # 产生一个返回值true
print(['a', 'b'] in lt)  # 产生一个返回值false 说明in只能判断一个值或者子list是否在list中

# 判断某个元素在list中，然后删除
lt = ['aa', 'a', 'a', 'b', 'c', 'd', 'a']
ind = input("请输入想要查询的元素")
if ind in lt:
    lt.remove(ind)
    print(lt)
else:
    print('"%s"元素不在list中' % ind)

# range(start,	stop[,	step])是一个内置函数 生成一个数组
lt = range(5)
print(lt)  # python3中range()返回值不是一个列表  打印出来的结果:range(0, 5)

  #  要打印出list需要用list转化
lt = range(5)  # range(5) == range(0, 5, 1)
print(list(range(5)))  # [0, 1, 2, 3, 4]

 # range()函数中生成的数组不包含stop的值


# list的排序 list.sort(cmp=None,	key=None,	reverse=False)
# sorted(iterable[,	cmp[,	key[,	reverse]]])

# 在python3中，sort是对于列表类型的排序函数，函数原型为：L.sort(key=None, reverse=False)，
# 该方法没有返回值，是对列表的就地排序。
lt = [1, 4, 6, 3, 2]
lt.sort()  # 直接改变了list的顺序
print(lt)
lt = [1, 4, 6, 3, 2]
lt.sort(reverse=True)  # True and False 需要大写.不能小写 # 倒序
print(lt) # [6, 4, 3, 2, 1]

# 2、python3中sorted函数取消了对cmp的支持,sorted 可以对所有可迭代的对象进行排序操作，
# 尤其是可以对字典进行排序，其形式为：sorted(iterable, key=None, reverse=False)。sorted函数是有返回值的。
lt = [1, 4, 6, 3, 2]
print(sorted(lt, reverse=True))  # 倒序

lt = [1, 4, 6, 3, 2]
lt1 = sorted(lt)  # 正序
print(lt1)  # [1, 2, 3, 4, 6]

# list 和 str 的区别
# list和str的最大区别是：list是可以改变的，str不可变。
# list和str的相同点是: 都是序列型数据

# list和str转化
# str.split(self, /, sep=None, maxsplit=-1) 将文本分隔成list
line = 'you are a sb.\nyes,you are right.'
print(line)
print(line.split('.', 1))  # ['you are a sb', '\nyes,you are right.']

line = 'you are a sb.\nyes,you are right.'
print(line)
print(line.split(' ', 1))  # ['you', 'are a sb.\nyes,you are right.'] 1表示最多分隔2次

line = 'you are a sb.\nyes,you are right.'
print(line)
print(line.split())  # 默认按照分隔符来分隔单词

# 将list合成文本 "[sep]".join(list) sep表示加入的分隔符
line = 'you are a sb.\nyes,you are right.'
lt = line.split()
print(lt)
print(' '.join(lt))  # you are a sb. yes,you are right.


# list解析
# 可以用简单的语言写出list
# 将下面的语句用list解析写出来
lt = []
for i in range(1, 101):
    if i % 3 == 0:
        lt.append(i)
print(lt)
print("100以内总共有%d个被3整除的数" % len(lt))
# 改写后的语句
lt = [i for i in range(1, 101) if i % 3 == 0]
print(lt)
print("100以内总共有%d个被3整除的数" % len(lt))

# 去掉 mybag = [' glass',' apple','green leaf ']中元素中的空格
mybag = [' glass', ' apple', 'green leaf ']
new_mybag = [i.strip() for i in mybag]
print(new_mybag)

# 到1到9的每个整数的平方
lt = [i ** 2 for i in range(1, 10)]
print(lt)

# enumerate函数 可以同时得到元素编号和元素怎么办 enumerate()函数是返回值type类型为enumerate,需用list转换
# 得到序列中的每个元素的编号和内容
week = ['Monday', 'Sunday', 'Friday']
for i in range(len(week)):
    print('%d' % i + ':' + week[i])

week = ['Monday', 'Sunday', 'Friday']
lt = list(enumerate(week))
print(lt)  # [(0, 'Monday'), (1, 'Sunday'), (2, 'Friday')]

week = ['Monday', 'Sunday', 'Friday']
lt = list(enumerate(week, start=1))  # 可以用start改变序号开始值
print(lt)  # [(1, 'Monday'), (2, 'Sunday'), (3, 'Friday')]

# 用函数的方法写


def couple(pos, element):
    return "%d : %s" % (pos, element)


week = ['Monday', 'Sunday', 'Friday']
lt = [couple(i, n) for i, n in enumerate(week)]
print(lt)   # ['0 : Monday', '1 : Sunday', '2 : Friday']

# 错误写法
week = ['Monday', 'Sunday', 'Friday']
lt = []
lt = [lt.append('%d : %s' % (i, n)) for i, n in enumerate(week)]
print(lt)  # [None, None, None]














