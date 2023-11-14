"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""


def input_in_new_file() -> None:
    """
    the function creates a file (if it does not exist) and writes the data entered by the user line by line into it
    функия создаёт файл(если его нет) и записывает в него построчно введённые пользователем данные
    :return: None
    """

    print('=' * 15 + 'task_01' + '=' * 15)

    with open('text_01.txt', 'w', encoding='utf-8') as f:
        num_line = 1
        usr_data = 'N/D'
        while usr_data:
            if usr_data := input(f'{num_line} line. Enter data to write to file:'):
                print(usr_data, file=f)
                num_line += 1


def count_words_and_lines(file_name: str) -> None:
    """
    count the lines and words in a file
    подсчёт строк и слов в файле
    :return: None
    """

    print('=' * 15 + 'task_02' + '=' * 15)

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            count_words = 0
            for n, line in enumerate(f):    # TODO возможно нужно посчитать и последнюю пустую строку при её наличии
                print(f'line №{n + 1}: {len(line.split())} words')
                count_words += len(line.split(" "))
    except IOError:
        print('An I/O error has occurred')

    print('total lines:', n + 1)
    print('total words:', count_words)


def main():
    file_name = 'text_01.txt'
    input_in_new_file()
    count_words_and_lines(file_name)


if __name__ == '__main__':
    main()
