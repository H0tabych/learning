"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается,
сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст(не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NotNumber(Exception):

    def __init__(self, text):
        self.text = text

    @classmethod
    def validation(cls, usr_list):
        num_list = []

        for i in usr_list:
            test = i.replace('.', '', 1).replace('-', '', 1) if i[0] == '-' else i.replace('.', '', 1)
            if not test.isdigit():
                try:
                    raise cls(f'{i} is not number')
                except NotNumber:
                    print(f'{i} is not number. number skipped')
            else:
                num_list.append(float(i))

        return num_list


def main():

    num_list = []
    out_text = 'Q'
    out = False
    while not out:
        user_input = input('Enter numbers separated by spaces, enter Q/q to exit:').upper().split()

        if out_text in set(user_input):
            num_list.extend(NotNumber.validation(user_input[:user_input.index(out_text)]))
            out = True
            continue
        else:
            num_list.extend(NotNumber.validation(user_input))

    print(num_list)


if __name__ == '__main__':
    main()
