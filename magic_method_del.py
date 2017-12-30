class Foo(object):

    def __init__(self):
        print('foo __init__')
        return None

    def __del__(self):
        print('foo __del__')

foo = Foo()
foo.__del__()
print(foo)
del foo
print(foo)  # NameError: name 'foo' is not defined
