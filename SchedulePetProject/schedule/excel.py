import os.path

import openpyxl
from django.conf import settings

from .models import Group


def get_ws():
    path = os.path.join(settings.EXCEL_ROOT, 'schedule.xlsx')
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    return ws


def get_cell_value(sheet, letter, num):
    return str(get_merged_value(sheet, sheet[f'{letter}{num}']))


def get_merged_value(sheet, cell):
    rng = [s for s in sheet.merged_cells.ranges if cell.coordinate in s]
    return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng) != 0 else cell.value


def get_day_schedule(sheet, day_start, group):
    result_dict = ['<br>1 пара<br>',
                   '<br>2 пара<br>',
                   '<br>3 пара<br>',
                   '<br>4 пара<br>',
                   '<br>5 пара<br>',
                   '<br>6 пара<br>']
    for i in range(len(result_dict)):
        for j in range(day_start, day_start + 3):
            if get_cell_value(sheet, group, j) != 'None':
                result_dict[i] += get_cell_value(sheet, group, j) + '\n'
            else:
                result_dict[i] += '\n'

        day_start += 3
    return ''.join(session for session in result_dict)


def get_week_schedule(sheet, group, cell_start=16):
    result = ['<br>Понедельник<br>',
              '<br>Вторник<br>',
              '<br>Среда<br>',
              '<br>Четверг<br>',
              '<br>Пятница<br>',
              '<br>Суббота<br>'
              ]

    for i in range(len(result)):
        result[i] += get_day_schedule(sheet, cell_start, group)
        cell_start += 25

    return ''.join(s for s in result)


def get_week_all_groups_schedule(sheet):
    result_dict = {
        "23ИСИТ 1гр": {},
        "23ИСИТ 2гр": {},
    }
    for key in result_dict:
        result_dict[key] = get_week_schedule(sheet, RANGES_GROUPS[key][0])
    return result_dict


def insert_schedule():
    data_dict = get_week_all_groups_schedule(get_ws())
    print(data_dict)
    group = Group.objects.get(title='23ИСИТ 1гр')
    group.content = data_dict['23ИСИТ 1гр']


RANGES_GROUPS = {"23ИСИТ 1гр": 'd',
                 "23ИСИТ 2гр": 'e',
                 "23ПИ 1гр": 'f',
                 "23ПИ 2гр": 'g',
                 }
