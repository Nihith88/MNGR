import sys
import os
import datetime

def ls_fldr():
    return os.listdir(os.getcwd())

def cr_fldr(usr_dir_name):
    usr_dir_name = (input('Введите название новой папки') if str else 'Новая папка')
    os.mkdir(os.path.join(os.getcwd(), usr_dir_name))

def rm_fldr():
    pass

def copy_fldr():
    pass

def lvl_up():
    pass

def ch_dir():
    pass


def cr_file():
    pass

def rm_file():
    pass

def copy_file():
    pass