# 文件的打开
f = open("F:\\Python\\练习\\110.txt")
print(type(f))
print(f.read())
f.close()

f = open("F:\\Python\\练习\\110.txt")
for line in f:
    print(line)
