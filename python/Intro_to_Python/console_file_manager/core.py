import os
import shutil
import datetime


def create_file(name: str, text=''):
    """
    Функция создания файла
    :param name: наименование файла
    :param text: текст,который будет записан в файл
    :return:
    """
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)


def create_folder(name):
    """
    Функция создания папок
    :param name: наименование папки
    :return:
    """
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже есть")


def get_list(folders_only=False):
    """
    Функция просмотра содержимого папки
    :param folders_only: файл или только папка
    :return:
    """
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    """
    Функция удаления файлов или папок
    :param name: наименование папки или файла
    :return:
    """
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    """
    Функция копирования файлов или папок
    :param name: наименование копируемого файла или папки
    :param new_name:
    :return:
    """
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    """
    Функция логирования
    :param message: сообщение
    :return:
    """
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f1')
    get_list()
    delete_file('new_f1')
    delete_file('text.dat')
    copy_file('new_f', 'new2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('abs')
