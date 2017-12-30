try:
	print(1)
	print(10 / 0)
except ZeroDivisionError:
	print(unknow_var)
finally:
	print("This is executed last")