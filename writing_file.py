file = open("newfile.txt", "w")
file.write("This has been writtern to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()