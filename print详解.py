# eval()的用法  字符串中符合python表达式的东西计算出来
eval('6+4')  # 10
'6+4'  # '6+4'
'"add" + "four"'
eval('"add" + "four"')  # addfour

# exec(),这个函数专门来执行字符串或文件里面的python语句。
exec("print('hahah')")  # hahah
"print('hahah')"  # "print('hahah')"




