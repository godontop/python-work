file = open("trip_way.py", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()