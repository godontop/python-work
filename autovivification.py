class AutoVivification(dict):
    """Implementation of perl's autovivification."""

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

weather = AutoVivification()
weather['china']['guangdong']['shenzhen'] = 'sunny'
weather['china']['hubei']['wuhan'] = 'sunny'
weather['USA']['California']['Los Angeles'] = 'sunny'
print(weather)
