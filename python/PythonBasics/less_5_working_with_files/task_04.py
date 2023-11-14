"""
Usage googletrans version 4.0.0rc1

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from googletrans import Translator


def main():
    translator = Translator()
    try:
        with open('text_4.txt', 'r', encoding='utf-8') as f:
            with open('text_4_ru.txt', 'w', encoding='utf-8') as f_ru:
                while line := f.readline():
                    result = translator.translate(line.split()[0], dest='ru')
                    print(result.text, *line.split()[1:], file=f_ru)
    except IOError:
        print('An I/O error has occurred')


if __name__ == '__main__':
    main()
