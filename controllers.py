from menu import *
from notebook import *
from form import *

nb = NoteBook('bd.json', 'note_book.txt')

def process_func():
    check_new_data = False
    while True:
        if check_new_data:
            msg = 'ВНИМАНИЕ! Сохраните внесенные изменения в файл!'
            div = '*' * len(msg)
            print(div, msg, div, sep='\n')
        menu_main = main_menu.show()
        match menu_main:
            case 1:
                nb.show_notes(nb.dict)
            case 2:
                print('find note')
            case 3:
                data_note = get_note.get_data()
                nb.add_note(data_note)
                check_new_data = True
            case 4:
                print('edit note')
            case 5:
                print('delete note')
            case 6:
                nb.save()
                check_new_data = False
            case 7:
                print('Работа с приложением Заметки завершена.')
                return False