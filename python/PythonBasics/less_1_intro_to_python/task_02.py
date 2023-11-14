"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
"""

second_in_hour = 3600
second_in_minute = 60

# Запрос у пользователя времени в секундах
user_time = int(input("Пожалуйста, введите время в секундах: "))

# Перевод user_time в формат чч:мм:сс
user_time_hh = int(user_time // second_in_hour)
user_time_mm = int((user_time - user_time_hh * second_in_hour) // second_in_minute)
user_time_ss = int(user_time % second_in_minute)

print(f'Введённое время в секундах, конвертировано в формат "чч:мм:сс", и составляет:'
      f' {user_time_hh:02}:{user_time_mm:02}:{user_time_ss:02}')
