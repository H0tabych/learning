def profile_user(name_f: str, age_f: int, city_f: str):
    return f'{name_f}, {age_f} год(а), проживает в городе {city_f}'


name = input('Введите имя: ')
age = int(input(f'Введите возраст {name}: '))
city = input(f'Введите город, в котором проживает {name}: ')

print(profile_user(name, age, city))
