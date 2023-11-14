"""
Пользователь вводит любое натуральное число.
Находим наибольшую цифру в числе.
"""

# Запрос числа у пользователя
user_num = int(input("Введите любое натуральное число: "))

max_num = 0
rem_num = user_num
this_num = 0

# цикл поиска наибольшего числа
while rem_num - 10 > -10:
    this_num = rem_num % 10
    rem_num //= 10
    if max_num < this_num:
        max_num = this_num

print(max_num)
