def sum(x):
	res = 0
	for i in range(x):
		res += i
#		return res
	return res
# Don't put the return in for loop, or the for loop will just run one time,
# then quit.

print(sum(10))