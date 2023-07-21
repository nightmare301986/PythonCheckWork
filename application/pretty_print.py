"""

\nДоступные методы:
\npt_print_all() - вывод всех записок.
\npt_print_filter_date() - вывод всех записок в соответствии с датой (по уменьшению).
\npt_print_id_date() - вывод ID и даты последненго изменения.
\npt_print_id_selection() - вывод записки с ее ID.
"""

from datetime import datetime
from prettytable import PrettyTable
from .logger import logging

SORTED_PRINT_TIP = 'Отсортированные по дате заметки печатаются в виде таблицы в консоли.'
NO_VALID_FILE = 'Нет допустимого файла для чтения.'


def pt_print_all(data_notes: dict) -> None:

    try:
        table = PrettyTable()
        table.field_names = list(data_notes['notes'][0].keys())
        for item in data_notes['notes']:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info('Заметки, напечатанные в виде таблицы в консоли.')
    except TypeError as error:
        print(error)
        logging.exception(error)
    except KeyError as err:
        print(NO_VALID_FILE)
        logging.exception(err)


def pt_print_filter_date(data_notes: dict) -> None:

    try:
        sorted_notes = sorted(data_notes['notes'], key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True)
        table = PrettyTable()
        table.field_names = list(sorted_notes[0].keys())
        for item in sorted_notes:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)


def pt_print_id_date(data_notes: dict) -> None:

    try:
        sorted_notes = sorted(data_notes['notes'], key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True)
        table = PrettyTable()
        all_fields = list(sorted_notes[0].keys())
        table.field_names = [_ for _ in all_fields if _ in ['id', 'date']]

        for item in sorted_notes:
            table.add_row([item[i] for i in table.field_names])

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)
    except IndexError as index_err:
        print('Не найден файл для удаления')
        logging.exception(index_err)
        return -1


def pt_print_id_selection(data_notes: dict, idx: int) -> None:

    try:
        table = PrettyTable()
        table.field_names = list(data_notes['notes'][0].keys())

        for item in data_notes['notes']:
            if item.get('id') == idx:
                table.add_row([item[i] for i in table.field_names])

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)
