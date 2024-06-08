class Menu:
    def __init__(self):
        self.__menu_items = {}

    def __get_choice(self):
        print()
        for cmd, (_, description) in self.__menu_items.items():
            print(f'{cmd} - {description}')

        print('0 - Exit')
        return input('Enter number in brackets: ')

    def add_handler(self, cmd, description):
        def wrapper(func):
            self.__menu_items[cmd] = (func, description)
            return func

        return wrapper

    def run(self):
        while True:
            choice = self.__get_choice()
            if choice == '0':
                break
            func, _ = self.__menu_items.get(choice, (default, ''))


menu = Menu()

# TODO functions for actions


def default():
    print('Something went wrong! Try again please.')

