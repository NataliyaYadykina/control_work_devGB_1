import json
import os
from note import Note

class NoteBook:
    def __init__(self, path: str, export_path: str) -> None:
        self.path = path
        self.export_path = export_path
        self.empty_book_message = 'Заметки не найдены.'
        self.dict = self.load()

    # Получение данных из файла .json в словарь
    def load(self):
        if os.stat(self.path).st_size == 0:
            notes_db = {}
        else:
            notes_db = json.load(open(self.path, 'r', encoding='utf-8'))
        return notes_db

    # Просмотр заметок
    def show_notes(self, data_notes):
        title = 'Все заметки'
        separ = '-' * len(title)
        print(separ, title, separ, sep='\n')
        print()
        if not data_notes:
            print(self.empty_book_message)
        else:
            for id, note_info in data_notes.items():
                print(f'{id}. {note_info[0]}\n   {note_info[1]}\n   Дата создания: {note_info[2]}\n   Дата изменения: {note_info[3]}')

