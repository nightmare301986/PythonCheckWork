"""
\n
\nAДоступные методы:
\nmain_menu() - UI главного меню.
\nchoose_option() - выбор операции.
\nask_about_filename() - ввод имени файла UI.
\nselect_id_ui() - выбор ID UI.
\nask_for_title() - диалог ввода заголовка записки UI.
\nask_about_data() - диалог ввода тела записки UI.
\nnote_added_ui() - информация (допролнительная) о записке UI.
\nask_about_filename_for_read() - диалог выбора имени файла записки для вывода на экран UI.
\nask_about_filename_for_save() - диалог выбора имени файла записки для сохранения UI.
\ndata_saved() - информация о сохранении записки UI.
\nask_about_data_edit() - диалог изменения записки UI.
\nedit_title_note_ui() - диалог изменения названия (заголовки)записки UI.
\nedit_data_note_ui() - диалог изменения записки UI.
\ndata_deleted() - запрос удаления записки UI.
"""

import sys
from .validator import validation_mode, validation_operation, validation_filename, validation_id, validation_data, \
    validate_edit

MAX_SYMBOLS_TITLE = 25
MAX_SYMBOLS_DATA = 50


def main_menu() -> None | tuple[int, int]:

    print("""Приложение для заметок. Управляйте своими заметками в одном месте.


Выбор:
1 - открыть сохраненную записку (файл)
2 - добавить записку
3 - редактировать
4 - сохранить
5 - удалить

0 - выход
""")

    mode = validation_mode()
    if mode == 0:
        print(f'Примечание Приложение завершено с кодом выхода {mode}')
        sys.exit()
    return choose_option(mode)


def choose_option(main_mode: int) -> None | tuple[int, int]:

    if main_mode in [1]:
        print("""Выбор опции для чтения (просмотра) записок
1 - вывести все записки в консоль
2 - вывести все записки (по дате)
3 - вывести выбранную записку

0 - пердыдущее меню
""")
    operation = validation_operation(main_mode)
    if operation in [10]:
        return main_menu()
    return main_mode, operation


def ask_about_filename() -> str:

    print("""Введите имя файла.

Пожалуйста, введите имя файла без расширения
или нажмите enter, чтобы использовать имя файла по умолчанию: примечания

Допускаются только цифры и буквы.
Расширение файла должно быть .json
""")
    return validation_filename()


def select_id_ui(data: dict) -> int:

    print("""Пожалуйста, введите идентификатор заметки, которую вы хотите выбрать.
Доступные идентификаторы представлены в таблице выше.
""")
    return validation_id(data)


def ask_for_title() -> str:

    print(f"""Какое название вы хотите для своей заметки?
Максимальное количество символов равно {MAX_SYMBOLS_TITLE}
""")
    return validation_data(MAX_SYMBOLS_TITLE)


def ask_about_data() -> str:

    print(f"""Напечатайте что-нибудь в своей заметке
Максимальное количество символов равно {MAX_SYMBOLS_DATA}
""")
    return validation_data(MAX_SYMBOLS_DATA)


def note_added_ui() -> None:

    print('Добавлена новая заметка!')


def ask_about_filename_for_read() -> str:

    print("""Введите имя файла для считывания данных.

Пожалуйста, введите имя файла без расширения
или нажмите enter, чтобы использовать имя файла по умолчанию: примечания

Допускаются только цифры и буквы.
Расширение файла должно быть .json
""")
    return validation_filename()


def ask_about_filename_for_save() -> str:

    print("""Введите имя файла для сохранения данных.

Пожалуйста, введите имя файла без расширения
или нажмите enter, чтобы использовать имя файла по умолчанию: примечания

Допускаются только цифры и буквы.
Расширение файла должно быть .json
""")
    return validation_filename()


def data_saved(srs: str) -> None:

    print(f"""Данные будут сохранены.
Вы найдете данные в следующем источнике:
{srs}
""")


def ask_about_data_edit() -> int:

    print("""Параметры для редактирования
1 - отредактировать заголовок
2 - редактирование данных

0 - предыдущее меню
""")
    operation = validate_edit()
    if operation in [30]:
        return main_menu()
    return operation


def edit_title_note_ui() -> str:

    print("""Введите новое название заметки.
Допускаются только цифры и буквы.
""")
    return validation_data(MAX_SYMBOLS_TITLE)


def edit_data_note_ui() -> str:

    print("""Введите новые данные для примечания.
Допускаются только цифры и буквы.
""")
    return validation_data(MAX_SYMBOLS_DATA)


def data_deleted(srs: str) -> None:

    print(f"""Данные удалены.
Вы найдете данные в следующем источнике:
{srs}
""")
