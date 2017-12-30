"""
str.join(iterable)
Return a string which is the concatenation of the strings in iterable.
A TypeError will be raised if there are any non-string values in iterable,
including bytes objects. The separator between elements is the string
providing this method.
"""
a = "alike"
b = "bike"
c = "Cisco"
print("\n".join([a, b, c]))
