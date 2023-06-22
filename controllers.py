from menu import *

def process_func():
    while True:
        menu_main = main_menu.show()
        match menu_main:
            case 1:
                print('show all notes')
            case 2:
                print('find note')
            case 3:
                print('add note')
            case 4:
                print('edit note')
            case 5:
                print('delete note')
            case 6:
                print('The end')
                return False