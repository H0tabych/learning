"""
Пользователь вводит любое натуральное число n.
Находим сумму n + nn + nnn.
"""

iter_sum = 2  # количество операций суммирования
out_sum = 0

# Запрос числа у пользователя
user_num = input("Введите любое натуральное число: ")

# Расчёт суммы n + nn + nnn
while iter_sum >= 0:
    out_sum += int((iter_sum + 1) * user_num)
    iter_sum -= 1

print(out_sum)
