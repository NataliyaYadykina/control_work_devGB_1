from datetime import datetime

class Note:
    def __init__(self, data_note: list) -> None:
        self.title = data_note[0]
        self.content = data_note[1]
        self.add_date = str(datetime.now()).split('.')[0]
        self.edit_date = ""

    def __str__(self) -> str:
        return f'{self.title:<20} | {self.content:<60} | Создано: {self.add_date:<20} | Изменено: {self.edit_date:<20}'

# note = Note(['title_note', 'content_note', datetime.now(), ''])
# print(note)