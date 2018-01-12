# 在while循环中，break的作用也是一样的。
for i in range(1, 6):
    print 'i =', i,
    print 'Hello, how',
    if i == 3:
        break
    print 'are you today?'
