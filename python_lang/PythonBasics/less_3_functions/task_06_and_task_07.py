"""
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
Дополнительные материалы
"""


def verification(list_words):
    """
    function to check the list of words against lowercase letters in words
    функция проверки списка слов на соответствие строчным буквам в словах
    :param list_words: checked list
    :return: True or False
    """
    set_unicode = set(range(ord('a'), ord('z')+1))
    for s in list_words:
        for i in s:
            if ord(i) not in set_unicode:
                print('the string you entered does not only consist of small Latin letters')
                print('program terminated ahead of schedule')
                return False
    return True


def int_funk(words):
    """
    function that changes the first letter of the words in the list to capital
    функция изменяющая первую букву слов списка на заглавную
    :param words: word list
    :return: capitalized string of words
    """
    mod_string = ' '.join(list(map(lambda s: s.capitalize(), words)))
    return mod_string


def main():
    """
    Main program function
    Основная функция программы
    :return: None
    """
    list_words = list(input('Please enter words from lowercase latin letters separated by spaces: ').split())
    list_words = list(map(lambda s: s.strip(), list_words))
    if verification(list_words):
        print(int_funk(list_words))


if __name__ == '__main__':
    main()
