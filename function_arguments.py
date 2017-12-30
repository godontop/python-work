"""
The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.
"""


def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)


def function2(named_arg, *cl):
    print(named_arg)
    print(cl)

function2(4, 5, 6, 7, 8)
