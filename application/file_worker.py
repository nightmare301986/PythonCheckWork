"""

\nДоступные методы:
\nwrite_to_file() - записать в файл.
\nload_from_file() - загрузить данные в программу.
"""

import json
from .logger import logging


def write_to_file(data: dict, source: str) -> None:

    try:
        with open(source, 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, ensure_ascii=False)
        logging.info(f'Запись данных в {source}')
    except FileNotFoundError as err:
        print(f'Источник {source} не найден. Отмена')
        logging.exception(err)
        return -1
    except OSError as err:
        print(f'Произошла ошибка при попытке открыть {source}')
        logging.exception(err)
        return -1
    except Exception as error:
        print(f'Неожиданная ошибка открытия {source} ошибка', repr(error))
        logging.exception(error)
        return -1


def load_from_file(source: str) -> dict:

    try:
        with open(source, encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f'Считывание данных из {source}')
        return data
    except json.decoder.JSONDecodeError as jsonerr:
        print(jsonerr)
        logging.exception(jsonerr)
        return -1
    except FileNotFoundError as err:
        print(f'Источник {source} не найден. Отмена')
        logging.exception(err)
        return -1
    except OSError as oserr:
        print(f'Произошла ошибка операционной системы при попытке открыть {source}')
        logging.exception(oserr)
        return -1
    except Exception as excerr:
        print(f'Неожиданная ошибка открытия {source} ошибка', repr(excerr))
        logging.exception(excerr)
        return -1
