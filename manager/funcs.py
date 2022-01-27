import main
import os
import shutil
import datetime

def get_log(event=None):
    cur_time = datetime.datetime.now()
    result = f'{cur_time} -> {event}'
    with open(main.logfilename, 'a', encoding='utf-8') as lf:
        lf.write(result, '\n')


def cr_fldr():  # Создание папки с пользовательским именем
    name = input('Введите название новой папки')
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует')


def rm_fldr():   # удаление папки с указанным именем
    usr_dir_name = input('Введите название папки для удаления')
    os.rmdir(usr_dir_name)


def copy_fldr():
    name = input('Введите название папки для копирования')
    new_name = input('Введите название новой папки')
    try:
        shutil.copytree(name, new_name)
    except FileExistsError:
        print('такая папка уже существует')


def get_list():
    print(os.listdir())


def cr_file(text=None):  # Создание файла с возможностью записи некоторого текста
    filename = input('Введите название для нового файла с расширением')
    with open(filename, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def rm_file():
    name = input('Введите название файла для удаления')
    os.remove(name)


def copy_file():
    name = input('Введите название файла для копирования')
    new_name = input('Введите название нового файла')
    try:
        shutil.copy(name, new_name)
    except FileExistsError:
        print('Такой файл уже существует')