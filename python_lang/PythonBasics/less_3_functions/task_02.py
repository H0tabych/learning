"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def output_profile(name, surname, birth_year, city, email, phone_number):
    """
    Function to display user information
    Функция вывода информации о пользователе
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone_number: int
    :return: None
    """
    print(f'name: {name}, surname: {surname}, birth_year: {birth_year}, '
          f'city: {city}, email: {email}, phone_number: {phone_number}')


def main():
    """
    Main program function
    Основная функция программы
    """

    fields = ['name', 'surname', 'birth_year', 'city', 'email', 'phone_number']
    user_data = {k: input(f'Input {k}: ') for k in fields}
    output_profile(name=user_data['name'], surname=user_data['surname'], birth_year=user_data['birth_year'],
                   city=user_data['city'], email=user_data['email'], phone_number=user_data['phone_number'])


if __name__ == '__main__':
    main()
