# 给用户三次机会，猜想我们程序生成的一个数字 A，
# 每次用户猜想过后会提示数字是否正确以及用户输入数字是大于还是小于A，
# 当机会用尽后提示用户已经输掉了游戏

import random
num = random.randint(1, 10)
num_in = input("请输入一个1-10之间的数字")
while True:
    if num_in.isdigit():
        for i in range(0, 3):
            if int(num_in) == num:
                print("恭喜你,猜对了")
                break
            elif int(num_in) > num:
                print('你猜的数字偏大,你还有{0}次机会'.format((2 - i)))
                if i == 2:
                    break
                num_in = int(input("请重新输入一个数字"))
            elif int(num_in) < num:
                print('你猜的数字偏小,你还有{0}次机会'.format((2 - i)))
                if i == 2:
                    break
                num_in = int(input("请重新输入一个数字"))
        print('游戏结束!!\n系统随机到的数字为%d' % num)
        break
    else:
        print('您输入的不是数字,请输入一个数字.\n请重新输入')
        num_in = input("请输入一个1-10之间的数字")

# 面向对象的编程(完整程序在  猜数字_面向对象编程.py 中)
# 下面为思考过程
# 1.用户 -行为输入数字


class Users:
    number_in = 0

    def input_num(self):
        print('请输入一个数字')
        self.number_in = input()
        return self.number_in

    def judgment_number(self):
        if self.number_in.isdigit():
            return True
        else:
            return False


chengyu = Users()  # 创建一个chengyu用户

# 最初的思路  --不能循环输入数字,只能输入两次数字
chengyu.input_num()  # 用户输入一个数字
if chengyu.judgment_number():  # 如果用户输入的为一个数字则继续
    pass
else:
    chengyu.input_num()  # 输入不是数字则继续输入

# 后来的思路
chengyu.input_num()
while not chengyu.judgment_number():  # 不是数字时候转入循环输入数字
    chengyu.input_num()

# 2.系统
import random


class System:
    def __init__(self, limit_down, limit_up, times):  # 初始化函数时候选择猜测游戏的范围和次数
        self.random_number = random.randint(limit_down, limit_up)
        self.times = times

    def judge_num(self, number):
        if self.random_number == number:
            print('恭喜你猜对了!!')
            return False
        elif self.random_number < number:
            print('输入的数值偏大')
        else:
            print('输入的数值偏小')

    def judge_num_times(self, use_time):
        residual_time = self.times - use_time
        if residual_time == 0:
            print('你的次数已用完')
            return False
        else:
            print('你还有%d次机会' % residual_time )


chengyu_system = System(1, 10, 3)

# 写一个程序打印出0-100奇数
print(range(0, 101, 2))

# 设计一个验证用户密码的程序，用户只有三次机会输入错误，不过如果用户输入的内容包括 “*” 则不计算在内
code = 'chengyu'
times = 3
for i in range(0, times):
    input_word = input('请输入密码')
    while True:
        if '*' in input_word:
            input_word = input('请输入密码')
        else:
            break
    if input_word == code:
        print('欢迎!!')
        break
    else:
        print('密码错误,你还有%d次机会.' % (times - i))

# 另外一种写法
code_one = 'xx01'
time = 3
while time:
    input_one = input('Please enter the password !!')
    if '*' in input_one:
        print('输入的密码中不能有*号')
    elif input_one == code_one:
        print('Congratulations')
        break
    else:
        print('密码错误!!')
        time -= 1





























