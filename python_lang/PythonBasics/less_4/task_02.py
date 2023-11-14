"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint


def filter_list(orig_list: list) -> list:
    """
    a function that filters the elements of the input list, leaving those that are greater than the previous one
    функция фильтрующая элементы входного списка, оставляя те, которые больше предыдущего
    :param orig_list: list
    :return: list
    """
    result_list = [orig_list[n] for n in range(1, len(orig_list)) if orig_list[n] > orig_list[n - 1]]
    return result_list


def main():
    original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    rand_list = [randint(-100, 100) for _ in range(len(original_list))]
    print('original list:', original_list)
    print('filtered list:', filter_list(original_list))
    print('original random list:', rand_list)
    print('filtered random list:', filter_list(rand_list))


if __name__ == '__main__':
    main()
