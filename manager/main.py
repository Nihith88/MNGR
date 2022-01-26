import os, datetime, time
import manager.funcs
print(70*'=')
print(21*' ', 'КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР', 21*' ')
print(12*' ', 'СОЗДАНИЕ КОПИРОВАНИЕ И УДАЛЕНИЕ ФАЙЛОВ И ПАПОК', 12*' ')
print(20*' ', 'СОХРАНЕНИЕ СВОЕЙ РАБОТЫ В ФАЙЛ', 20*' ')
print(70*'=', '\n')

usrname = input('Введите имя пользователя для ведения отчета:  ')
logfilename = ('log_' + usrname + '_' + '.log')
lf = open(logfilename, 'w')
lf.write('Сессия начата в ' + str(time.ctime()))
lf.close()
choise = '0'
while choise != 'x':
      print(usrname, 'Вы находитесь в каталоге ', os.getcwd(), '\n \n')
      print('1 - посмотреть содержимое папки, 2 - создать папку, 3 - удалить папку, 4 - создать копию папки \n'
            '5 - на уровень вверх, 6 - перейти в папку по имени, 7 - создать файл, 8 - удалить файл, '
            '9 - скопировать файл, p - сыграть в игру, x - выход \n')
      choise = input()
      if choise == '1':  #
            print(str(os.listdir(os.getcwd())))
      elif choise == '2':  #
            manager.funcs.cr_fldr()
      elif choise == '3':  #
            manager.funcs.rm_fldr()
      elif choise == '4':  #
            manager.funcs.copy_fldr()
      elif choise == '5':  #
            manager.funcs.lvl_up()
      elif choise == '6':  #
            manager.funcs.ch_dir()
      elif choise == '7':  #
            manager.funcs.cr_file()
      elif choise == '8':  #
            manager.funcs.rm_file()
      elif choise == '9':  #
            manager.funcs.copy_file()
      elif choise == 'p':  #
            pass
      else:  #
            break

