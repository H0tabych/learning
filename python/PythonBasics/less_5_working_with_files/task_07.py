"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

from verification import isfloat
import json


def main():
    try:
        with open('text_7.txt', 'r', encoding='utf-8') as f:
            profitability = dict()
            average_profitability = dict()
            while data := f.readline().split():
                if isfloat(*data[2:]):
                    profitability[data[0]] = (float(data[2]) - float(data[3]))

        positive_profit = {k: v for (k, v) in profitability.items() if v >= 0}
        average_profitability['average_profitability'] = sum(positive_profit.values())/len(positive_profit)
        result = [profitability, average_profitability]

        with open('text_7_result.json', 'w', encoding='utf-8') as f_json:
            json.dump(result, f_json, indent=4, ensure_ascii=False)

    except IOError:
        print('An I/O error has occurred')


if __name__ == '__main__':
    main()
