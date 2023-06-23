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

    # Добавление заметки
    def add_note(self, data_note):
        note = Note(data_note)
        if self.dict:
            max_id = int(max(self.dict, key=int))
        else:
            max_id = 0
        self.dict[str(max_id + 1)] = [note.title, note.content, note.add_date, '']
        print(f'\nЗаметка #{max_id + 1} успешно добавлена!\n')

    # Сохранение данных словаря в файл .json и экспорт в текстовый файл
    def save(self):
        json.dump(self.dict, open(self.path, 'w', encoding='utf-8'), ensure_ascii=False)
        str_note = ''
        for id, note_info in self.dict.items():
            str_note += f'{id}. {note_info[0]}\n   {note_info[1]}\n   Дата создания: {note_info[2]}\n   Дата изменения: {note_info[3]}\n'
            str_note += '\n'
        print(str_note)
        with open(self.export_path, 'w', encoding = 'utf-8') as f:
            f.write(str_note)
        print('Заметки успешно сохранены в файл.')