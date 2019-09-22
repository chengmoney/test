# for循环
# for循环的结构
"""
for	循环规则：
    操作语句
"""
line = 'hello, I am chengyu'
for i in line:
    print(i, end=' ')  # 打印出line字符串中所有的单词,并以空格分隔开来

# 打印出line中的每个单词
line = 'hello, I am chengyu'
lt = line.split()  # 将line字符串分隔成list
print(lt)
for i in lt:
    print(i)  # 按照单词打印


# 例：找出100以内的能够被3整除的正整数。
n = 0
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
        n = n + 1
print("100以内总共有%d个被3整除的数"%n)

lt = []
for i in range(1, 101):
    if i % 3 == 0:
        lt.append(i)
print(lt)
print("100以内总共有%d个被3整除的数" % len(lt))





