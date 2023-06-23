from menu import *
from notebook import *

nb = NoteBook('bd.json', 'note_book.txt')

def process_func():
    while True:
        menu_main = main_menu.show()
        match menu_main:
            case 1:
                nb.show_notes(nb.dict)
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