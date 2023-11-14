"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
#### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count, cycle


def generate(start: int, stop: int) -> list:
    """
    A function that generates a list using an infinite loop with a given start
    Функция генерирующая список с помощью бесконечного цикла с заданным началом
    :param start: start generate
    :param stop: stop generate
    :return: result list
    """
    gen_list = []
    for el in count(start):
        if el > stop:
            return gen_list
        else:
            gen_list.append(el)


def repetitions_list(data_set: list, repetition_count: int) -> None:
    """
    a function that iterates over the elements of a list a specified number of times
    функция проходящая по элементам списка заданное количество раз
    :param data_set: input list
    :param repetition_count: number of iterations
    :return: None
    """
    n = 0
    for el in cycle(data_set):
        if n > repetition_count:
            break
        else:
            print(el)
            n += 1


def main():
    start_generate = 3
    stop_generate = 7
    repetitions = 18
    gen_list = generate(start_generate, stop_generate)
    print('generated list:', gen_list)
    repetitions_list(gen_list, repetitions)


if __name__ == '__main__':
    main()
