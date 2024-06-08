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


menu = Menu()

# TODO realize functions for actions
@menu.add_handler('1', 'Зареєструватися')
def menu_register():
    pass


@menu.add_handler('2', 'Увійти')
def menu_login():
    pass


@menu.add_handler('3', 'Вийти')
def menu_exit():
    pass


def default():
    print('Невідома дія. Будь-ласка, спробуйте ще раз.')

