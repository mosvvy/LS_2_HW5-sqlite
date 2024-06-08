from user import User


class Menu:
    def __init__(self):
        self.__menu_items = {}

    def __get_choice(self):
        print()
        for cmd, (_, description) in self.__menu_items.items():
            print(f'{cmd} - {description}')

        return input('Введіть номер дії: ')

    def add_handler(self, cmd, description):
        def wrapper(func):
            self.__menu_items[cmd] = (func, description)
            return func

        return wrapper

    def run(self):
        while True:
            choice = self.__get_choice()
            if choice == '3':
                break
            func, _ = self.__menu_items.get(choice, (default, ''))
            func()


menu = Menu()


# TODO realize functions for actions
@menu.add_handler('1', 'Зареєструватися')
def menu_register():
    """Якщо користувач обирає зареєструватися, програма має
    запитати username, password та email,
    створити нового користувача і зберегти його в базу даних."""
    username = input('Введіть ім\'я користувача: ')
    password = input('Введіть пароль: ')
    email = input('Введіть адресу ел.пошти: ')
    new_user = User(username, password, email)
    new_user.register()


@menu.add_handler('2', 'Увійти')
def menu_login():
    """Якщо користувач обирає увійти, програма має запитати username та password,
    потім перевірити, чи існує такий користувач у базі даних.
    Якщо так, вивести повідомлення "Успішний вхід!", інакше - "Неправильні дані!" """
    username = input('Введіть ім\'я користувача: ')
    password = input('Введіть пароль: ')
    new_user = User(username, password, None)
    login_result = new_user.login(username, password)
    if login_result:
        print('Успішний вхід!')
    else:
        print('Неправильні дані!')


@menu.add_handler('3', 'Вийти')
def menu_exit():
    pass


def default():
    print('Невідома дія. Будь-ласка, спробуйте ще раз.')


if __name__ == '__main__':
    menu.run()
