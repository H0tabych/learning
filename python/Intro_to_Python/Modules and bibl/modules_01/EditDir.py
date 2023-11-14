import os


def new_dir(name, amount):
    for num in range(amount):
        os.mkdir(f'{name}_{num+1}')


def del_dir(name, amount):
    for num in range(amount):
        os.rmdir(f'{name}_{num+1}')
