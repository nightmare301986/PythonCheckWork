"""

\nДоступные методы
\ncheck_data_storage() - проверка папки и файла записки
\ncheck_folder() - проверка существования папки с запиской
\ncheck_notes_json() -  проверка существования папки с записки
\nfill_notes() - заполнение тестовыми данными
\nfill_new_note() - добавление новой информации в записку
\nfill_dict() - разделение полей данных в файле записки
\nupdate_note() - выбор действий
\nupdate_title() - обновление названия записки
\nupdate_data() -  обновление данных (информации) записки
\nnote_deletion() - удаление данных
"""

from os import path, makedirs
from typing import Any
from .logger import logging
from .file_worker import write_to_file

DEFAULT_DIRNAME = './Data_store/'
DEFAULT_FILENAME = 'notes.json'
DEFAULT_EXTENSION = '.json'
DEFAULT_SRC = DEFAULT_DIRNAME + DEFAULT_FILENAME
TEST_DATA_JSON = {"notes": [
    {"id": 1, "title": "Купить хлеб", "data": "Мне нужно купить хлеба на завтрак", "date": "19-07-2023"},
    {"id": 2, "title": "Call teacher", "data": "Ask about mistakes found in my homework.", "date": "09-02-2023"},
    {"id": 8, "title": "Ask Mark about his life", "data": "I should call my old friend Mark this friday.",
     "date": "13-02-2023"},
    {"id": 12, "title": "Use time machine", "data": "Use time machine to travel back to the past.",
     "date": "01-01-1990"}]}


def check_data_storage() -> None:
    
    logging.info('Проверка данных.')
    check_folder()
    check_notes_json()
    logging.info('Данные проверены.')


def check_folder() -> None:
    
    try:
        if not path.exists(DEFAULT_DIRNAME):
            makedirs(DEFAULT_DIRNAME)
            logging.info(f'Папка {DEFAULT_DIRNAME} создана.')
    except OSError as error:
        print(f'нельзя создать {DEFAULT_DIRNAME} директорию', error)
        logging.exception(f'нельзя создать {DEFAULT_DIRNAME} директорию', error)


def check_notes_json() -> None:
    
    try:
        if not path.exists(DEFAULT_SRC):
            fill_notes()
            logging.info(f'Файл {DEFAULT_FILENAME} записки создан в папке {DEFAULT_DIRNAME}.')
    except OSError as error:
        print(f'Не удалось создать {DEFAULT_FILENAME} файл', error)
        logging.exception(f'Не удалось создать {DEFAULT_FILENAME} файл', error)


def fill_notes() -> None:
   
    try:
        write_to_file(TEST_DATA_JSON, DEFAULT_SRC)
    except Exception as fillerr:
        print(fillerr)
        logging.exception(fillerr)
    logging.info(f'Записка записана в файле {DEFAULT_FILENAME}.')


def generate_filesource(custom_filename: str) -> str:
    
    try:
        custom_src = DEFAULT_DIRNAME + custom_filename + DEFAULT_EXTENSION
    except Exception as err:
        print(err)
        logging.exception(err)
    return custom_src


def fill_new_note(data: dict, note_id: int,
                  note_title: str, note_data: str, date: str) -> dict:
   
    new_note = fill_dict(('id', note_id), ('title', note_title), ('data', note_data), ('date', date))
    data['notes'].append(new_note)
    return data


def fill_dict(*args: Any) -> dict:
    
    return {arg[0]: arg[1] for arg in args}


def update_note(mode: int, data: str, notes: dict, id_note: int) -> dict:
    
    if mode in [31]:
        return update_title(data, notes, id_note)
    if mode in [32]:
        return update_data(data, notes, id_note)


def update_title(new_title: str, notes: dict, id_note: int) -> dict:
   
    for i in range(len(notes['notes'])):
        if notes['notes'][i].get('id') == id_note:
            notes['notes'][i]['title'] = new_title
            return notes


def update_data(new_data: str, notes: dict, id_note: int) -> dict:
    
    for i in range(len(notes['notes'])):
        if notes['notes'][i].get('id') == id_note:
            notes['notes'][i]['data'] = new_data
            return notes


def note_deletion(note_id: int, notes: dict) -> dict:
    
    for i in range(len(notes['notes'])):
        if notes['notes'][i].get('id') == note_id:
            new_notes = notes['notes'][:i] + notes['notes'][-1:i:-1]
    notes['notes'] = new_notes
    return notes
