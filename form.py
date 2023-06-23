import text_fields

class Form:
    def __init__(self, text_field: str) -> None:
        self.text_field = text_field

    # Получение данных заметки от пользователя
    def get_data(self):
        data_note = []
        list_fields = self.text_field.split('\n')
        for field in list_fields:
            flag = True
            while flag:
                data_str = input(field)
                if data_str:
                    data_note.append(data_str)
                    flag = False
                else:
                    print('Поле не должно быть пустым!')
        return data_note

# Получение данных заметки
get_note = Form(text_fields.data_new_note)