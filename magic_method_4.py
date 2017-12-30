# _*_ coding: utf-8 _*_
from datetime import datetime
import pickle


class Distance(object):

    def __init__(self, meter):
        print('distance __init__')
        self.meter = meter

data = {
    'foo': [1, 2, 3],
    'bar': ('Hello', 'world!'),
    'baz': True,
    'dt': datetime(2016, 10, 1),
    'distance': Distance(1.78),
}
print('before dump:', data)
with open('data.pkl', 'wb') as jar:
    pickle.dump(data, jar)  # 将数据存储在文件中

del data
print('data is deleted!')

with open('data.pkl', 'rb') as jar:
    data = pickle.load(jar)  # 从文件中回复数据
print('after load:', data)
