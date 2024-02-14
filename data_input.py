import pprint


class PhoneBook:
    """
        Класс для телефонного справочника
        Содержит:
            список всех контактов
            функции добавления контактов
            поиска контактов
            изменение контактов
            удаления контактов
    """
    def __init__(self):
        self.command: str = input("Введите команду: ")

    @staticmethod
    def my_decor(func):
        """Декоратор для функций вывода"""
        def wrapper(*args):
            print(f"\n˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜\n")
            print(func(*args))
            print(f"\n˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜˜”*°•.•°*”˜\n")
        return wrapper

    @my_decor
    def user_action(self):
        """Функция ответа на команды введённые пользователем"""

        match self.command:
            case '1':
                return self.show_book()
            case '2':
                return self.add_user()
            case '3':
                correct_cont: str = input('Введите Фамилию/Имя/Отчество/ для изменения: ')
                return self.correct_contact(correct_cont)
            case '4':
                search_cont: str = input('Введите Фамилию/Имя/Отчество/организацию для поиска: ')
                return self.search_user(search_cont)
            case '5':
                del_cont: str = input('Введите Фамилию/Имя/Отчество/организацию для УДАЛЕНИЯ: ')
                return self.user_delete(del_cont)
            case _:
                return "ОШИБКА : Нет такой команды!"

    @staticmethod
    def add_user() -> list:
        """Функция добавления контакта"""

        new_entry_in_book: dict = {
                    1: "Введите Ваше ФИО: ",
                    2: "Введите организацию если есть : ",
                    3: "Введите рабочий телефон: ",
                    4: "Введите сотовый телефон: "
                }
        new_list_entry: list = []
        for i in range(1, len(new_entry_in_book) + 1):
            x: str = input(new_entry_in_book[i])
            if x != '':
                new_list_entry.append(x)
            else:
                new_list_entry.append('Отсутствует')

        with open("Contacts.txt", "+a", encoding="UTF-8") as file:
            file.write(', '.join(new_list_entry) + '\n')
        return new_list_entry

    @staticmethod
    def show_book() -> str:
        """ Показывает список записей справочника """
        with open('Contacts.txt', 'r', encoding='UTF-8') as file:
            read_lines: list = sorted(file.readlines())
            count: int = 0
            print(' ☜(˚▽˚)☞  Телефонный справочник  ☜(˚▽˚)☞  \n')
            while len(read_lines) > count:
                try:
                    for i in range(5):
                        if read_lines[i + count]:
                            print("".join(read_lines[i + count]))

                    count += 5
                    print('▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼')
                    input("Следующая страница Enter ....\n")

                except IndexError:
                    print('\nБольше записей нет!\n'
                          '▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄ ▀▄')
                    break
                except KeyboardInterrupt:
                    print('Завершение просмотра справочника')
        return '\nКонец справочника!'

    def search_user(self, request: str, comnd=True):
        """ Функция поиска контакта """

        with open('Contacts.txt', 'r', encoding='UTF-8') as file:
            rf = file.read()
        result: list = []

        for i in rf.split('\n'):
            for elem in i.split(','):
                if request.lower() in elem.lower() and len(request) > 1:
                    if i is not result:
                        result.append(i + '\n')

        if result and comnd:
            return '\n'.join(set(result))
        elif result and not comnd:
            return set(result)

        return (f"Результат поиска контакта\n"
                f"      ¯\_(ツ)_/¯     \n"
                f"* Нет такого контакта *\n")

    def create_dict_list_users(self, request):
        """Создание словаря с найдеными контактами"""
        
        list_user = self.search_user(request, comnd=False)

        if isinstance(list_user, set):
            dict_user: dict = {}
            key_du: int = 1
            for st in list_user:
                dict_user[key_du] = st.replace('\n', '')
                key_du += 1
            pprint.pprint(dict_user)
        else:
            return list_user

        while True:
            try:
                choice_is_yours = int(input("Выберите цифру контакта для редактирования: "))
                match 0 < choice_is_yours <= len(dict_user):
                    case True: break
                    case False: print('Неправильно выбран контакт')
            except ValueError:
                print("Неправильный ввод попробуйте ещё раз!")

        return dict_user[choice_is_yours]

    def correct_contact(self, request: str) -> str:
        """Функция редактирования контакта"""

        correct_users = self.create_dict_list_users(request)

        with open('Contacts.txt', 'r', encoding='UTF-8') as file1:
            lines = file1.readlines()

        for line in lines:

            if correct_users in line:
                print(f"для редактирования выбран = {line}")

                new_dict_user: list = []

                for entry in correct_users.split(','):
                    new_entry: str = input(f'Текущее {entry}  -  Enter если не изменять\nВведите новое значение : ')
                    if new_entry != '':
                        new_dict_user.append(new_entry)
                    else:
                        new_dict_user.append(entry)

                lines.remove(line)
                lines.append(','.join(new_dict_user) + '\n')

                with open('Contacts.txt', 'w', encoding='UTF-8') as file2:
                    for i in lines:
                        file2.write(i)

                return 'Запись изменена!'

    def user_delete(self, request: str) -> str:
        """Функция удаления пользователя"""
        del_users = self.create_dict_list_users(request)

        with open('Contacts.txt', 'r', encoding='UTF-8') as file1:
            lines = file1.readlines()

        for line in lines:
            if del_users in line:
                print(f"для удаления выбран = {line}"
                      f"Введите < да >, если уверены\n"
                      f"Введите < нет >, если отменить")

                while True:
                    question: str = input('Что выберешь ?  ')
                    match question.lower():
                        case 'да' | 'yes' | 'y':
                            lines.remove(line)
                            with open('Contacts.txt', 'w', encoding='UTF-8') as file2:
                                for i in lines:
                                    file2.write(i)
                            return '\nЗапись УДАЛЕНА!'

                        case 'нет' | 'no':
                            return 'Запись не удалена!'
                        case _:
                            print('Не правильный ввод')
