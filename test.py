week = ['Monday', 'Sunday', 'Friday']
lt = []
lt1 = [lt.append(str(i) + n) for i, n in enumerate(week)]
print(lt1)

lt = []
for i, n in enumerate(week):
    lt.append('%d : %s' % (i, n))
print(lt)


# 用print输出以下文字：
# 1.
# He said, "I'm yours!"
# 2.
# \\_v_//
# 3.
# Stay hungry,
# stay foolish.
#     -- Steve Jobs
# 4.
# *
# ***
# *****
# ***
# *
word = 'He said,"I\'m yours!"'
print(word)

face = '\\\_v_//'
print(face)

word = '''Stay hungry,
stay foolish.
    -- Steve Jobs
'''
print(word)





