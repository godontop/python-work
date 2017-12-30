file = open("filename.txt", "r")

#print(file.readlines())

for line in file:
	print(line)
# In the output, the lines are separated by blank lines, as the print 
# function automatically adds a new line at the end of its output.

file.close()