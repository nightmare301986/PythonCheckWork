"""
\nThis module validates all user input data.
\nДдоступные методы:
\nvalidation_mode() - проверяет ввод для режима главного меню.
\nvalidation_operation() - проверяет вводимые данные на соответствие режиму работы.
\ninvalidate_read() - проверяет вводимые данные на предмет чтения.
\ninvalidate_add_note - проверяет вводимые данные для добавления примечания.
\nvalidate_edit_note() - проверяет вводимые данные для редактирования заметки.
\ninvalidate_save_note() - проверяет вводимые данные для сохранения заметки.
\ninvalidate_delete_note() - проверяет вводимые данные на предмет удаления примечания.
\nvalidation_id() - проверяет вводимый идентификатор заметки.
\nvalidate_edit() - проверяет вводимые данные для режима редактирования.
"""

from .logger import logging

AVAILABLE_MODES_MAIN_MENU = 6
MUST_BE_INTEGER = 'Неверный ввод! Входные данные должны быть целыми числами.'
INCORRECT_INPUT = 'Неверный ввод! Пожалуйста, ознакомьтесь с доступными режимами.'
NO_VALID_FILE = 'Нет допустимого файла для чтения.'


def validation_mode() -> int:

    while True:
        try:
            main_menu_mode = int(input('Какой режим вам нужен:'))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if main_menu_mode in range(AVAILABLE_MODES_MAIN_MENU):
            if main_menu_mode == 0:
                logging.info('Завершите работу из главного меню.')
            else:
                logging.info(f'Основной режим интерфейса = {main_menu_mode}')
            return main_menu_mode
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)


def validation_operation(main_menu_mode: int) -> int:
    
    match main_menu_mode:
        case 1:
            return validate_read()
        case 2:
            return 21
        case 3:
            return 31
        case 4:
            return 41
        case 5:
            return 51
        case _:
            logging.INFO(INCORRECT_INPUT)


def validate_read() -> int:

    number_of_available_modes = 4
    while True:
        try:
            operation_type = int(input('Введите код операции: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'Код операции для считывания = {operation_type + 10}')
            return operation_type + 10
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)


def validation_filename() -> str:

    while True:
        try:
            filename = input('Введите имя файла: ').strip()
        except Exception as err:
            print('Что-то пошло не так при чтении имени файла. Пробовать снова.')
            logging.exception(err)
            continue
        if not filename:
            print('Чтение файла по умолчанию.')
            logging.info('Чтение файла по умолчанию.')
            return filename
        elif not filename.isalnum():
            print('Пожалуйста, используйте в имени файла только буквы и цифры.')
            logging.info(f'Неправильное имя файла {filename}.')
            continue
        print(f'Допустимо для чтения {filename = }.')
        logging.info(f'Допустимо для чтения {filename = }.')
        return filename


def validation_id(data: dict) -> int:

    while True:
        try:
            available_ids = [data['notes'][i]['id'] for i in range(len(data['notes']))]
            selected_id = int(input('Введите id записки: '))
            if selected_id in available_ids:
                logging.info(f'{selected_id = }')
                return selected_id
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        except TypeError as error:
            print('Неправильное имя файла')
            logging.exception(error)
            return -1
        except KeyError as error:
            print(NO_VALID_FILE)
            logging.exception(error)
            break;
        print('Неверный идентификатор! Пожалуйста, ознакомьтесь с доступными идентификаторами в таблице выше.')
        logging.exception('Неверный идентификатор! Пожалуйста, ознакомьтесь с доступными идентификаторами в таблице выше.')


def validation_data(max_symbols: int) -> str:

    while True:
        try:
            fill_data = input(f'Type something. Max {max_symbols} characters: ')
        except Exception as err:
            print('Something went wrong when collecting data. Try again.')
            logging.exception(err)
            continue
        if len(fill_data) in range(max_symbols + 1):
            logging.info(f'Введенные данные для примечания {fill_data = } с длиной = {len(fill_data)}.')
            return fill_data
        print(f'Максимальное количество символов равно {max_symbols}.')
        logging.info(f'введенные данные для примечания {fill_data = } с длиной = {len(fill_data)}.')


def validate_edit() -> int:

    number_of_available_modes = 3
    while True:
        try:
            operation_type = int(input('Введите код операции: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'Код операции для считывания = {operation_type + 30}')
            return operation_type + 30
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)
