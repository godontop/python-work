motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
# 函数对列表所做的更改是实时的、永久性的，列表变量调用方法后，其值就永久性的
# 变化了！字符串变量调用方法后，其原本的值并未改变。
print(motorcycles)
print(popped_motorcycle)