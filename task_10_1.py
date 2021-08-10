"""
Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+.
"""

from csv_utils import *


@get_csv_field(field_name='Возраст', fields=['Имя', 'Фамилия', 'Возраст'])
def get_age(_row):
    pass


@get_csv_field(field_name='Имя', fields=['Имя', 'Фамилия', 'Возраст'])
def get_name(_row):
    pass


@get_csv_field(field_name='Фамилия', fields=['Имя', 'Фамилия', 'Возраст'])
def get_soname(_row):
    pass


def get_stat(_rows, _age_groups, _fields):
    """ Функция - создания словаря статистики возрастных групп """
    age_stat = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # Словарь для статистики возрастных групп

    def key_func(x):
        """ Вспомогательная функция """
        for i in range(1, len(_age_groups.keys()) + 1):  # Цикл для количества ключей
            if _age_groups[i]['low'] <= x <= _age_groups[i]['high']:  # Проверка вхождения в группу
                return i  # если условие выполнимо то вернуть номер группы
        return 0  # Вернуть общее значение если ни одно условие не выполнимо

    # Перекодирование списка
    all_groups_age = [i for i in list(map(key_func, [int(get_age(row)) for row in _rows]))]

    for i in range(1, len(_age_groups.keys()) + 1):  # Цикл для подсчета статистики
        age_stat[i] = all_groups_age.count(i)  # Запомнить статистику

    return age_stat  # Вернуть словарь со значениями


def print_stat(age_stat, _age_groups):
    """ Функция - для печати словаря на экране с поянениями """
    sum_all = 0  # Инициализация общего количесва записей
    for i in range(1, len(_age_groups.keys()) + 1):  # # Цикл для вывода словаря
        sum_all += age_stat[i]  # Подсчёт количесва записей
        # Вывод на экран
        print(f'In group {i} of age from {_age_groups[i]["low"]} '
              f'to {_age_groups[i]["high"]} are {age_stat[i]} people')
    print('Total people: ', sum_all)  # Вывод на экран


def save_report(_filename, age_stat, _age_groups):
    """ Функция - для сохранения отчёта в формате .htm"""
    # Начало формата
    li_lines_beg = [
        '<html>',
        '   <head>',
        '   </head>',
        '   <body>',
    ]
    # Окончание формата
    li_lines_end = [
        '   </body>',
        '</html>',
    ]
    with open(_filename, 'w') as my_file:  # Открыть файл на запись
        my_file.writelines(li_lines_beg)  # Записать начало формата
        my_file.write('<i>')  # Записать тег
        sum_all = 0  # Инит
        for i in range(1, len(_age_groups.keys()) + 1):  # Цикл по ключам словаря
            sum_all += age_stat[i]  # Подсчёт количества записей
            # Вывод в файл
            my_file.write(f'In group {i} of age from {_age_groups[i]["low"]} '
                          f'to {_age_groups[i]["high"]} are {age_stat[i]} people <br>')
        my_file.write(f'<br>Total people: {sum_all}')  # Вывод в файл
        my_file.write('</i>')  # Вывод в файл
        my_file.writelines(li_lines_end)  # Записать конец формата


def main_func():
    """ Test function """
    # Словарь возрастных групп
    age_group = {
        1: {'low': 1, 'high': 12},
        2: {'low': 13, 'high': 18},
        3: {'low': 19, 'high': 25},
        4: {'low': 26, 'high': 40},
        5: {'low': 40, 'high': 99},
    }

    fields, rows = read_csv('data/people.csv')  # Чтение текстового формата

    print('Name= ', get_name(rows[0]))
    print('Surname= ', get_soname(rows[0]))
    print('Age= ', get_age(rows[0]))

    print()  # Вывод пустой строки
    stat = get_stat(rows, age_group, _fields=fields)  # Получение словаря статистики
    print_stat(stat, age_group)  # Вывод на экран
    save_report('data/people_report.htm', stat, _age_groups=age_group)  # Сохранение отчёта в файл

    stat1 = {}
    for i in stat.keys():
        ii = int(i)
        old_value = stat[i]
        new_key = str(age_group[ii]['low']) + '_' + str(age_group[ii]['high'])
        stat1[new_key] = old_value

    save_json('data/people_report.json', stat1)


if __name__ == '__main__':
    main_func()
