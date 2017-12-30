def infinite_numbers():
    i = 10 ** 8
    while i > 1:
        yield i
        i -= 1

for i in infinite_numbers():
    print(i)
