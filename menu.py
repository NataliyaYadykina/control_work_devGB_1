import text_fields

class Menu:

    def __init__(self, text_menu: str) -> None:
        menu_strings = text_menu.split('\n')
        self.title = menu_strings[0]
        self.items = '\n'.join(menu_strings[1:-1])
        self.question = menu_strings[-1]

    def show(self) -> None:
        separator = '-' * len(self.title)
        print()
        print(separator, self.title, separator, self.items, self.question, sep='\n')
        length = len(self.items.split('\n'))
        while True:
            choice = input()
            if choice.isdigit() and 0 < int(choice) <= length:
                return int(choice)
            else:
                print(f'ОШИБКА! Введите значения от 1 до {length}:')

main_menu = Menu(text_fields.main_menu)
search_menu = Menu(text_fields.search_menu)