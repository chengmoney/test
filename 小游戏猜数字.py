# 开发一个猜数字游戏的程序。即程序在某个范围内指定一个数字，比如在0到9范围内指定一个数字，用户猜测程
# 序所指定的数字大小。
import random  # 引入random库
text = input('请输入一个0-9的整数')
pd = 1
num = random.randint(0, 9)  # random.randint(a,b)表示随机取得a-b之间的自然数
while pd == 1:
    if text.strip().isdigit():  # 判断输入的是否为数字或者整数
        text_num = int(text.strip())  # .strip()去掉空格

        if 0 <= text_num <= 9:  # 判断是否为0-9之间的数字
            if num > text_num:
                text = input('输入的值过小,重新输入')
            elif num < text_num:
                text = input("输入的值过大,请重新输入")
            else:
                pd = 0  # 跳出循环
                print('恭喜你,猜对了!')
        else:
            text = input("您输入的数字不在0-9的范围内,请重新输入")
    else:
        text = input("您输入的数据有误,请您重新输入一个0-9的整数")

