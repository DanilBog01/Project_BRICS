import pandas as pd
#Требует openpyxl

"""
TODO:
-Оптимизировать load_teams???
-Написать документацию модуля и функций
-Адаптировать названия в списках под наш формат данных
    --Только после перехода на новый формат таблиц excel!
    --Названия колонок - на латинице, подчёркивания вместо пробелов.
"""

players = ['ФИО', 'Балл за сезон', 'Стоимость контракта', 'Название команды']

def load_data_xl(columns):

    data = pd.read_excel('test_data.xlsx', usecols=columns)
    return data


def load_teams(players):

    teams = {}
    """
    teams - словарь. Должен содержать:
    Название команды - средний балл игроков - бюджет.
    взять из players -      высчитывать     - сумма + 20%
    """
    teams = pd.DataFrame(teams)
    return teams



if __name__ == '__main__':

    players = load_data_xl(players)
    teams = load_teams(players)

    print(players)
    print('\n')
    print(teams)
