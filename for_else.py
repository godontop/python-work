# else with for loop
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

# else with for loop
for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")
# With the for or while loop, the code within it is called if the loop finishes
# normally (when a break statement does not cause an exit from the loop).

# else with if statement
for i in range(10):
    if i == 999:
        break
    else:
        print("Unbroken 3")

# else with if statement
for i in range(10):
    if i == 5:
        break
    else:
        print("Unbroken 2")
# 注意看缩进，在前两个例子中else和for是平级的，所以for语句执行完了，才会执行else语句；
# 后面两个例子中else和if是平级的，所以if语句每次执行后，else也会相应地执行。
