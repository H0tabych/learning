"""
2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""

#  Запрос у пользователя ввести предложение, которое преобразуется в список,
#  элементами которого являются слова введённого предложения.
#  Затем вывод введённого предложения в терминал
my_list = input('Введите предложение, слова которого станут элементами списка: ').split()
print(my_list)

#  Цикл по списку с шагом 2 и условием чётности его длинны. В теле замена рядом стоящих элементов
for n in range(len(my_list) if len(my_list) % 2 == 0 else len(my_list)-1)[::2]:
    #  Меняем ссылки местами
    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]

#  Вывод получившегося списка
print(my_list)
