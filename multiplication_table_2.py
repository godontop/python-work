number = int(raw_input("Which table would you like? "))
upper = int(raw_input("How high do you want to go?"))
i = 1
print 'Here is your table:'
while i <= upper:
    print number, 'x', i, '=', number * i
    i += 1
