# -*- coding: utf-8 -*-
"""
Задание 4.2

Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX
в формат XXXX.XXXX.XXXX
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':', ".")
print (mac)
