# eval()的用法  字符串中符合python表达式的东西计算出来
eval('6+4')  # 10
'6+4'  # '6+4'
'"add" + "four"'
eval('"add" + "four"')  # addfour

# exec(),这个函数专门来执行字符串或文件里面的python语句。
exec("print('hahah')")  # hahah
"print('hahah')"  # "print('hahah')"


# 字符串的格式化 有两种形式 %d %s 和 format()

import math
print('圆周率为%d' % math.pi)  # 圆周率为3 %d只能输出整数
print('number is %d' % -1.5)  # number is -1
# 也可以用format()写
print('圆周率为{:.0f}'.format(math.pi))  # {:.0f}代表输出的数字精度f表示浮点数，.之前表示整数位保留多少位，.后表示小数点后精确到0
print('圆周率为{:.0f}'.format(-1.5))  # -2
print('圆周率为{0:d}'.format(56))  # 圆周率为56  format()中的数字必须为整数



