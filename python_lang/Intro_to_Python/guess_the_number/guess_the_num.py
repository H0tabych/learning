import random

min_max: tuple[int, int] = (1, 100)
number: int = int((min_max[1] - min_max[0])/2)
answer_user: str = ''
attempt_num: int = 1
winner_num: int = number

print('Пожалуйста, загадайте любое число от 1 до 100, \nа компьютер попытается его угадать.\n')

while answer_user != '=':
    print(f'Попытка угадать №{attempt_num}')
    answer_user = input(f'Загаданное вами число это {number}?\n Если да, то введите "=", '
                        f'если загаданное число меньше - введите "<", '
                        f'если оно больше, то введите ">": ')
    print()

    if answer_user == '=':
        continue
    elif answer_user == '<':
        min_max = (min_max[0], number - 1)
    elif answer_user == '>':
        min_max = (number + 1, min_max[1])

    number = random.randint(*min_max)
    attempt_num += 1
else:
    print(f'На попытке №{attempt_num}, число {number} было угадано! ')
