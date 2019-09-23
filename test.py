week = ['Monday', 'Sunday', 'Friday']
lt = []
lt1 = [lt.append(str(i) + n) for i, n in enumerate(week)]
print(lt1)

lt = []
for i, n in enumerate(week):
    lt.append('%d : %s' % (i, n))
print(lt)
