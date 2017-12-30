numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

h, i, *j, k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# A variable that is prefaced with an asterisk (*) takes all values from the
# iterable that are left over from the other variables.
print(h)
print(i)
print(j)
print(k)
