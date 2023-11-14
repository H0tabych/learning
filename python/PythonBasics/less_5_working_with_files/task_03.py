"""
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from verification import isfloat


def main():
    try:
        with open('text_3.txt', 'r', encoding='utf-8') as f:
            salary_sheet = dict()
            for n, line in enumerate(f):
                line = list(line.split())
                if isfloat(line[1]):
                    salary_sheet[line[0]] = float(line[1])
                else:
                    print(f'In line No. {n + 1} is not the correct value of the salary. Line skipped')
            if salary_sheet:
                less_20000 = list(filter(lambda val: val[1] < 20000, salary_sheet.items()))
                print(f'Employees with a salary of less than 20000 c.u.: '
                      f'{", ".join(list(zip(*less_20000))[0])}')
                print(f'Average salary of the employees: {sum(salary_sheet.values())/len(salary_sheet)} c.u.')
    except IOError:
        print('An I/O error has occurred')


if __name__ == '__main__':
    main()
