from menu import *
from notebook import *
from form import *

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
                data_note = get_note.get_data()
                nb.add_note(data_note)
            case 4:
                print('edit note')
            case 5:
                print('delete note')
            case 6:
                print('Работа с приложение Заметки завершена.')
                return False