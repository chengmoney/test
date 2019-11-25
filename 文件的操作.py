# 文件的打开
f = open("F:\\Python\\练习\\110.txt")
print(type(f))
print(f.read())
f.close()

f = open("F:\\Python\\练习\\110.txt")
for line in f:
    print(line)

# 读取文件
f = open('F:\\Python\\虚拟机密码.txt')
data = f.read()
print(data)
f.close()

# 用readline,readlines读取文件
f = open('F:\\Python\\1.自行安装运行环境.txt')
data = f.readline()  # 一行一行读取
print(data)
f.close()
# 用for循环读取
f = open('F:\\Python\\1.自行安装运行环境.txt')
for i in range(1, 20):
    data = f.readline()  # 一行一行读取
    print(data)
f.close()

# 用readlines
f = open('F:\\Python\\1.自行安装运行环境.txt')
data = f.readlines()
print(data)

# 用for循环读取readlines的内容
f = open('F:\\Python\\1.自行安装运行环境.txt')
data = f.readlines()
for line in data:
    if line != '\n':
        print(line, end='')
f.close()

# 写文件
file = open('F:\\Python\\myname.txt', 'w')
file.write('My name is cheng yu')
file.close()

# 从myname.txt中增加内容
file = open('F:\\Python\\myname.txt', 'a')
file.write('\nage is 29')
file.close()

# 把myname.txt中的内容另存到myname1.txt中
file1 = open('F:\\Python\\myname1.txt', 'w')  # 新建myname1.txt文件 w = writing
file = open('F:\\Python\\myname.txt')
data = file.read()  # 读取文件到data
file1.write(data)
file.close()
file1.close()

# -- scores.txt
# 刘备 23 35 44 47 51
# 关羽 60 77 68
# 张飞 97 99 89 91
# 诸葛亮 100
# 统计以上txt文件中每个学生的分数
f = open('F:\\Python\\练习\\分数汇总.txt')
data = f.readlines()
print(data)
out = open('F:\\Python\\练习\\分数汇总表.txt', 'w')
for line in data:
    lines = line.split()
    name = lines[0]
    score = []
    for sc in lines[1:]:
        score.append(int(sc))  # 将list中文本格式转换成int
    sum_score = sum(score)
    out_line = '{0}  {1}\n'.format(name, sum_score)
    out.write(out_line)
f.close()
out.close()

# continue 和 break的区别
i = 0
while i < 5:
   i += 1
   for j in range(3):
       print(j, end='')
       if j == 2:
           break
   print('')
   for k in range(3):
       if k == 2:
           continue
       print (k, end='')
    print('')
   if i > 3:
       break
   print (i)

