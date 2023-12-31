"""Действия с пользователем"""
from data_input import search_user, add_user, correct_contact, user_delete


def user_action(command):
    """Функция ответа на команды введённые пользователем"""

    if command == 1:
        with open("Contacts.txt", "r", encoding="UTF-8") as file_read:
            return print(f"****************************************************\n"
                         f"{file_read.read()}\n"
                         f"**************************************************** ")

    elif command == 2:
        print(f"***********************************************************\n"
              f"Запись добавлена = {add_user()}\n"
              f"***********************************************************")

    elif command == 3:
        correct_cont = input('Введите Фамилию/Имя/Отчество/ для изменения: ')
        print(f"***********************************************************\n"
              f"{correct_contact(correct_cont)}\n"
              f"***********************************************************")

    elif command == 3:
        search_cont = input('Введите Фамилию/Имя/Отчество/организацию для поиска: ')
        print(f"**********************************************************************\n"
              f"Результат поиска контакта\n"
              f"{search_user(search_cont)}\n"
              f"**********************************************************************\n")

    elif command == 5:
        del_cont = input('Введите Фамилию/Имя/Отчество/организацию для УДАЛЕНИЯ: ')
        print(f"**********************************************************************\n"
              f"{user_delete(del_cont)}\n"
              f"**********************************************************************")
    else:
        print(f'************************************************************\n'
              f'ОШИБКА : Нет такой команды!\n'
              f'************************************************************')


