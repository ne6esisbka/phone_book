def add_user():
    data_contacts = ['Введите ФИО = ', 'Введите название организации = ', 'Введите рабочий телефон = ',
                     'Введите телефон личный (сотовый) = ']
    new_user = [input(i) for i in data_contacts]

    with open("Contacts.txt", "+a", encoding="UTF-8") as file:
        file.write(f"{new_user}\n")
    return new_user


def search_user(su):
    """ Функция поиска контакта """

    reading_file = open('Contacts.txt', 'r', encoding='UTF-8')
    rf = reading_file.read()
    result = []

# разбиваем список по строчно
    for i in rf.split('\n'):
        if su.lower() in i.lower():
            result.append(i)


# проверяем если в переменной result значения
    if len(result) > 0:
        return result
    else:
        return (f"**********************************************************************\n"
                f"Результат поиска контакта\n"
                f"{{* Нет такого контакта *}}\n"
                f"**********************************************************************\n")


def correct_contact(cont):
    """Функция редактирования контакта"""

    res = 0
    with open('Contacts.txt', 'r', encoding='UTF-8') as file1:
        lines = file1.readlines()

    for line in lines:

        if cont in line:
            res += 1
            print(f"для редактирования выбран ={line}")
            lines.remove(line)
            add_cont = str(add_user())
            lines.append(f'{add_cont}\n')
            with open('Contacts.txt', 'w', encoding='UTF-8') as file2:
                for i in lines:
                    file2.write(i)
            return 'Запись изменена!'

    if res == 0:
        return 'Неправильный ввод!'


def user_delete(du):
    """Функция удаления пользователя"""

    with open('Contacts.txt', 'r', encoding='UTF-8') as file1:
        lines = file1.readlines()

    for line in lines:

        if du in line:
            print(f"для удаления выбран ={line}"
                  f"Введите да, если уверены\n"
                  f"Введите нет, если отменить")
            question = input('Что выберешь ?  ')
            if question.lower() == 'да' or question.lower() == 'yes':
                lines.remove(line)

                with open('Contacts.txt', 'w', encoding='UTF-8') as file2:
                    for i in lines:
                        file2.write(i)
                return 'Запись УДАЛЕНА!'
            elif question.lower() == 'нет' or question.lower() == 'no':
                return 'Вы сжалились'
            else:
                return 'Моя твоя не понимать! Попробуйте заново!'
