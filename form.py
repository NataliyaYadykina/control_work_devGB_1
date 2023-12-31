import text_fields

class Form:
    def __init__(self, text_field: str) -> None:
        self.text_field = text_field

    # Получение данных заметки от пользователя
    def get_data(self, edit = False) -> list:
        data_note = []
        list_fields = self.text_field.split('\n')
        for field in list_fields:
            flag = True
            while flag:
                data_str = input(field)
                if data_str or edit:
                    data_note.append(data_str)
                    flag = False
                else:
                    print('Поле не должно быть пустым!')
        return data_note

# Получение данных заметки для добавления
get_note = Form(text_fields.data_new_note)

# Получение даты заметки для поиска
get_date_note_for_search = Form(text_fields.note_date_for_search)

# Получение id заметки для поиска
get_id_note = Form(text_fields.note_id_for_search)