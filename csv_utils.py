import csv
from functools import wraps
import json


def field_index_by_name(_fields, _name):
    # print(_fields)
    for index, f in enumerate(_fields):
        if f.strip() == _name.strip():
            return index
    return -1


def get_csv_field(*args, **kwargs):
    fields = kwargs['fields']
    name = kwargs['field_name']

    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if field_index_by_name(fields, _name=name) != -1:
                index1 = field_index_by_name(fields, _name=name)
                return args[0][index1]
            else:
                return None

        return wrapper

    return decorate


def read_csv(_filename):
    """ Функция для чтения файла форматированных данных , формата ЦСВ"""
    rows = []  # Инит
    with open(_filename, 'r') as csv_file:  # Открыть файл для чтения
        csv_reader = csv.reader(csv_file)  # Чтение файла
        fields = next(csv_reader)  # Чтение заголовка
        for row in csv_reader:  # Повторять для каждой записи в файле
            rows.append(row)  # Запись добавить в список
        print("Total no. of rows: %d\n" % csv_reader.line_num)  # Вывести количество записей
        for col in fields:  #
            print("%10s" % col, end='')  # Вывести заголовки колонок
        print()  # Вывод пустой строки
    return fields, rows  # Вернуть заголовок и записи


def save_json(_filename, _dict):
    with open(_filename, 'w') as my_file:
        data = json.dumps(_dict)
        my_file.write(data)


def main_func():
    """ Test function """
    pass


if __name__ == '__main__':
    main_func()
