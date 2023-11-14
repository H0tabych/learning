import random
import math

"""
1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.
"""

fruit_1 = ['apple', 'banana', 'kiwi', 'plum', 'avocado']
fruit_2 = ['fig', 'apple', 'orange', 'avocado']

result_fruit = list(set(fruit_1) & set(fruit_2))
print(result_fruit)

print(30 * '#')

"""
2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, 
удовлетворяющих следующим условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.

Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 
10-20 чисел в списке вполне достаточно.
"""

rand_list = [random.randint(-100, 100) for x in range(10)]
print(rand_list)

new_list_1 = list(filter(lambda x: (x % 3 == 0) and (x > 0) and (x % 4 != 0), rand_list))
print(new_list_1)

new_list_2 = [x for x in rand_list if (x % 3 == 0) and (x > 0) and (x % 4 != 0)]
print(new_list_2)

print(30 * '#')

"""
3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней 
чисел (если число положительное) и самих чисел (если число отрицательное) и 
возвращает результат (желательно применить генератор и тернарный оператор при необходимости). 
В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]

Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 
10-20 чисел в списке вполне достаточно.
"""

rand_list = [random.randint(-100, 100) for x in range(10)]
print(rand_list)

new_list = [math.sqrt(x) if x > 0 else x for x in rand_list]
print(new_list)

print(30 * '#')

"""
4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13, 
функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число. 
Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция. 
Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
"""

number = int(input('Введите любое число: '))

try:
    if number != 13:
        print(number)
    else:
        raise ValueError
except ValueError:
    print('введено 13')
