"""
Завдання 1

Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином,
щоб у нього була основна частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс,
і модуль представлення, який відповідав би за взаємодію з користувачем.
При заміні останнього на інший, який взаємодіє
з користувачем в інший спосіб, програма має продовжувати коректно працювати.

"""

from mypcg import adding_to_lib, search_in, lib_out

my_lib = {}
while True:
    print("choose what to do:\n1) add items:\n2) search by name\n3) show all")
    option = input('choose options: ')
    if option == '1':
        adding_to_lib(my_lib)
    elif option == '2':
        print('what to search?')
        search_name = input("what name? ")
        search_in(my_lib, search_name)
    elif option == '3':
        lib_out(my_lib)
    else:
        print('end!')
        break