import random


class Users:
    number_in = 0

    def input_num(self):  # 用户输入数字的方法
        print('请输入一个数字')
        self.number_in = input()
        return self.number_in

    def judgment_number(self):  # 用户判断输入的是否是数字的方法
        return self.number_in.isdigit()


class System:
    def __init__(self, limit_down, limit_up, times):  # 初始化函数时候选择猜测游戏的范围和次数
        self.random_number = random.randint(limit_down, limit_up)
        self.times = times

    def judge_num(self, number):  # 判断用户输入的数值偏大还是偏小还是猜对了
        if self.random_number == number:
            print('恭喜你猜对了!!')
            return 1
        elif self.random_number < number:
            print('输入的数值偏大')
        else:
            print('输入的数值偏小')

    def judge_num_times(self, use_time):  # 判断用户还有多少次游戏机会
        residual_time = self.times - use_time
        if residual_time == 0:
            print('你的次数已用完,游戏结束')
            return False
        else:
            print('你还有%d次机会' % residual_time)
            return True


xiaowu = Users()  # 初始化
xiaowu_system = System(1, 10, 3)  # 下限为1,上限为10,游戏次数为3次

time = 0
for i in range(0, xiaowu_system.times):
    num = xiaowu.input_num()
    while not xiaowu.judgment_number():  # 如果不是数字返回False,进入循环重新输入
        print('输入的不是数字,请重新输入')
        num = xiaowu.input_num()
    temp_num = int(num)  # 将input输入的字符串格式的数字 转换成为 int
    time += 1  # 记取次数
    if xiaowu_system.judge_num(temp_num) == 1:  # 返回1代表猜对数字,跳出循环
        break
    else:
        xiaowu_system.judge_num_times(time)  # 告诉用户还有多少次机会

