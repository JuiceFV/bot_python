import command_system

def Coding():
   message = '''Материалы по структурке
   Разбивать на подразделы не буду, т.к. тут собрана вообщем-то вся информация, которая потребуется на двух ближайших курсах
   1) http://cppstudio.com/cat/274/'''
   return message, ''

Coding_com = command_system.Command()

Coding_com.keys = ['/прога','/программирование','/структурка']
Coding_com.description = 'Программирование'
Coding_com.process = Coding