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





