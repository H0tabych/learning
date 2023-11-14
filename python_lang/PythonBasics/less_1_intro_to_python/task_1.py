"""
Здесь просто играемся с переменными.
"""

a = 10
print(a, ' ', type(a))

b = 11.3
print(b, ' ', type(b))

tuple_ab = (a, b)
print(tuple_ab, ' ', type(tuple_ab))

list_ab = [a, b]
print(list_ab, ' ', type(list_ab))

auto = None
print(auto, ' ', type(auto))

data_bool = bool(auto)
print(data_bool, ' ', type(data_bool))

name = input('Введите свё имя: ')
age = int(input('Введите свой возраст: '))
profile = {'name': name, 'age': age}

print(profile, ' ', type(profile))
