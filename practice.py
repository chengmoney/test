# 1.	 接收任何字符和数字的输入
# 2.	 判断输入的内容，如果不是整数是字符，就告诉给用户；如果是小数，也告诉用户
# 3.	 如果输入的是整数，判断这个整数是奇数还是偶数，并且告诉给用户
# 在这个练习中，显然要对输入的内容进行判断，以下几点需要看官注意：
# 通过raw_input()得到的输入内容，都是str类型
# 要判断一个字符串是否是由纯粹数字组成，可以使用str.isdigit()（建议看官查看该内置函数官方文档）

# 判断一个文本是否为小数(1.有且只有一个小数点.  2.如果为负数只有一个-号 3.小数点前后均为数字


def isfloat(s):
    s = str(s)
    if s.isdigit():  # 判断是否为正整数
        return 2
    if s.count('-') == 1 and s.startswith('-'):  # 判断是否为负整数
        new_s = s.split('-')[-1]
        if new_s.isdigit():
            return 3
    if s.count(".") == 1:  # 数字只有一个小数点
        new_str = s.split('.')  # 将字符串按照.分隔成一个list
        right_str = new_str[-1]  # .右边的字符串
        left_str = new_str[0]  # .左边的字符串
        if right_str.isdigit():  # 判断右边字符串是否全部为数字组成
            if left_str.isdigit():  # 如果左右两边的字符串都为数字组成则为一个正有理数
                return 4
            elif left_str.count('-') == 1 and left_str.startswith("-"):  # 如果左边的不全为数字,有可能为负数.存在一个负号,且左边字符串第一个字符为-
                tmp_num = left_str.split('-')[-1]  # 分隔负号两边的字符串,并取出负号右边的字符串
                if tmp_num.isdigit():  # 如果负号右边的字符串全部为数字,则为负有理数
                    return 4
    return False


pd = 1
while pd == 1:
    text = input("请输入内容!")
    if isfloat(text) == 2 or isfloat(text) == 3:
        if int(text) % 2 == 0:
            print('输入的数字为一个整数,且输入的数字为偶数')
            break
        else:
            print('输入的数字为一个整数,且输入的数字为奇数')
            break
    elif isfloat(text) == 4:
        print('输入的数字为小数.')
        break
    else:
        print("您输入的内容不是一个有理数")



"""
def is_float(s):
    s = str(s)
    if s.count('.') == 1:
        new_s = s.split('.')
        left_num = new_s[0]
        right_num = new_s[-1]
        if right_num.isdigit():
            if left_num.isdigit():
                return True
            elif left_num.count('-')==1 and left_num.startswith('-'):
                tmp_num = left_num.split('-')[-1]
                if tmp_num.isdigit():
                    return True
    return False


s_in = input("请输入您要判断的字符串：\n")
print(is_float(s_in))
"""


