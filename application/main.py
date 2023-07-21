"""

\nДоступные методы:
\nentrance_point() - цикл в программе (для работы интерфейса).
\nmain_handler() - главные функции изменения.
\nhandler_for_read() - функции для чтения.
\nwait_for_continue() - ожидание завершения.
\nhandler_for_add() - добавление записи в файл.
\nhandler_for_save() - сохранение записи в файл.
\nhandler_for_edit() - изменение записи.
\nedit_switcher() - переключение вида изменения записи.
\nhandler_for_delete() - функции удаления.
"""

from datetime import datetime
from .logger import logging
from .user_interface import main_menu, ask_about_filename, select_id_ui, ask_for_title, ask_about_data, note_added_ui, \
    ask_about_filename_for_read, ask_about_filename_for_save, data_saved, ask_about_data_edit, edit_title_note_ui, \
    edit_data_note_ui, data_deleted
from .file_worker import write_to_file, load_from_file
from .data_checker_and_filler import check_data_storage, generate_filesource, DEFAULT_SRC, fill_new_note, update_note, \
    note_deletion
from .pretty_print import pt_print_all, pt_print_filter_date, pt_print_id_date, \
    pt_print_id_selection


def entrance_point() -> None:

    logging.info('Программ рабает.')
    check_data_storage()
    operation_type, operation_code = main_menu()
    logging.info(f'Выбор операции = {operation_type}, код операции = {operation_code}')
    main_handler(operation_code)
    logging.info('Выполнено')
    if operation_type != 0:
        entrance_point()


def main_handler(operation_code: int) -> None:

    if str(operation_code)[0] in ('1'):
        handler_for_read(operation_code)
    elif str(operation_code)[0] in ('2'):
        handler_for_add()
    elif str(operation_code)[0] in ('3'):
        handler_for_edit()
    elif str(operation_code)[0] in ('4'):
        handler_for_save()
    elif str(operation_code)[0] in ('5'):
        handler_for_delete()


def handler_for_read(operation_code: int) -> None:

    match operation_code:
        case 11:
            file_name_valid = ask_about_filename()
            print(file_name_valid)
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filesource(file_name_valid))
            try:
                if data_from_file == -1:
                    return -1
                data_from_file['notes'][0]
            except IndexError as err:
                print(err)
                logging.exception(err)
                return -1
            except KeyError as err:
                print(err)
                logging.exception(err)
                return -1

            pt_print_all(data_from_file)
            wait_for_continue()
        case 12:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filesource(file_name_valid))

            try:
                if data_from_file == -1:
                    return -1
                data_from_file['notes'][0]
            except IndexError as err:
                print(err)
                logging.exception(err)
                return -1
            except KeyError as err:
                print('Нет подходящего файла.')
                logging.exception(err)
                return -1

            pt_print_filter_date(data_from_file)
            wait_for_continue()
        case 13:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filesource(file_name_valid))

            try:
                if data_from_file == -1:
                    return -1
                data_from_file['notes'][0]
            except IndexError as err:
                print(err)
                logging.exception(err)
                return -1
            except KeyError as err:
                print(err)
                logging.exception(err)
                return -1

            pt_print_id_date(data_from_file)
            pt_print_id_selection(data_from_file, select_id_ui(data_from_file))
            wait_for_continue()


def handler_for_add() -> None:

    file_name_valid = ask_about_filename()
    if not file_name_valid:
        source = DEFAULT_SRC
        data_from_file = load_from_file(source)
    else:
        source = generate_filesource(file_name_valid)
        data_from_file = load_from_file(source)
    try:
        if data_from_file == -1:
            return -1
        note_id = data_from_file['notes'][-1]['id'] + 1
    except Exception as err:
        print(err)
        logging.exception(err)
        return -1
    finally:
        wait_for_continue()
    note_title = ask_for_title()
    note_data = ask_about_data()
    date = datetime.today().strftime('%d-%m-%Y')
    upd_data = fill_new_note(data_from_file, note_id, note_title, note_data, date)
    write_to_file(upd_data, source)
    note_added_ui()
    wait_for_continue()


def handler_for_save() -> None:

    file_name_valid = ask_about_filename_for_read()
    try:

        if not file_name_valid:
            source = DEFAULT_SRC
            data_from_file = load_from_file(source)
        else:
            source = generate_filesource(file_name_valid)
            data_from_file = load_from_file(source)
    except Exception as err:
        print(err)
        logging.exception(err)
        return -1
    finally:
        if data_from_file == -1:
            return -1
        wait_for_continue()

    filename_for_save = ask_about_filename_for_save()
    if not filename_for_save:
        source = DEFAULT_SRC
    else:
        source = generate_filesource(filename_for_save)
    try:
        write_to_file(data_from_file, source)
        data_saved(source)
        logging.info(f'Данные срхранены в {source=}')
    finally:
        wait_for_continue()


def handler_for_edit() -> None:

    file_name_valid = ask_about_filename_for_read()
    try:
        if not file_name_valid:
            source = DEFAULT_SRC
            data_from_file = load_from_file(source)
        else:
            source = generate_filesource(file_name_valid)
            data_from_file = load_from_file(source)
    except Exception as err:
        print(err)
        logging.exception(err)
        return -1
    finally:
        if data_from_file == -1:
            return -1
        wait_for_continue()

    try:
        data_from_file['notes'][0]
    except IndexError as err:
        print(err)
        logging.exception(err)
        return -1
    except KeyError as err:
        print(err)
        logging.exception(err)
        return -1

    pt_print_id_date(data_from_file)
    selected_id = select_id_ui(data_from_file)
    pt_print_id_selection(data_from_file, selected_id)
    wait_for_continue()

    option = ask_about_data_edit()
    edited_note = edit_switcher(option, data_from_file, selected_id)

    write_to_file(edited_note, source)
    pt_print_id_selection(edited_note, selected_id)
    data_saved(source)
    logging.info(f'Данные сохранены в {source=}')
    wait_for_continue()


def handler_for_delete() -> None:

    file_name_valid = ask_about_filename_for_read()
    try:
        if not file_name_valid:
            source = DEFAULT_SRC
            data_from_file = load_from_file(source)
        else:
            source = generate_filesource(file_name_valid)
            data_from_file = load_from_file(source)
    except Exception as err:
        print(err)
        logging.exception(err)
        return -1
    finally:
        if data_from_file == -1:
            return -1
        wait_for_continue()

    pt_print_id_date(data_from_file)

    try:
        data_from_file['notes'][0]
    except IndexError as err:
        print(err)
        logging.exception(err)
        return -1
    except KeyError as err:
        print(err)
        logging.exception(err)
        return -1
    selected_id = select_id_ui(data_from_file)
    update_notes = note_deletion(selected_id, data_from_file)

    write_to_file(update_notes, source)
    data_deleted(source)
    logging.info(f'Данные сохранены в {source=}')
    wait_for_continue()


def edit_switcher(mode: int, data: dict, id_note: int) -> dict:

    match mode:
        case 31:
            new_title = edit_title_note_ui()
            return update_note(mode, new_title, data, id_note)
        case 32:
            new_data = edit_data_note_ui()
            return update_note(mode, new_data, data, id_note)
        case _:
            logging.info('Неизвестная ошибка. Операция незавершена!')


def wait_for_continue() -> None:

    if input('Нажмите на любую клавишу: '):
        return
