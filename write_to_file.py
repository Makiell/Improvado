import csv
import json

# Словарь для перевода из численного значения пола в понятное строчное
SEX = {
    1: 'Woman',
    2: 'Man',
    0: 'Not specified',
}


def write_csv(path, friends, filename, first_request, file_number):

    # Название столбцов
    fieldnames = ['first_name', 'last_name', 'country', 'city', 'birth_date', 'sex']

    try:

        # Если это первая запись в файл, то записываем заголовок(название столбцов)
        if first_request:
            with open(f'{path}/{filename}_{file_number}.csv', 'w', encoding='utf-8') as file:
                writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames, lineterminator='\n')
                writer.writeheader()

        with open(f'{path}/{filename}_{file_number}.csv', 'a', encoding='utf-8') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames, lineterminator='\n')

            # Распарсиваем данные о каждом друге
            # Если какого то из полей 'country', 'city' или  'bdate' нету
            # то присваиваем им значение 'Unknown'
            for friend in friends:
                first_name = friend['first_name']
                last_name = friend['last_name']

                if 'country' in friend:
                    country = friend.get('country').get('title')
                else:
                    country = 'Unknown'

                if 'city' in friend:
                    city = friend.get('city').get('title')
                else:
                    city = 'Unknown'

                if 'bdate' in friend:
                    birthday = friend.get('bdate')

                    # Разделяем строку даты на элементы, чтобы узнать имеется ли год,
                    # если год имеется, то количество элементов будет равным 3
                    elements_count = birthday.split('.')

                    # Если год отсутствует, то прибавляем в строку значение 'YYYY',
                    # т.к. нам неизвестно какого года рождения друг
                    if len(elements_count) < 3:
                        birthday += '.YYYY'
                    day, month, year = birthday.split('.')

                    # ISO формат имеет вид YYYY-MM-DD
                    # поэтому если месяц или дата меньше 10, то добавляем спереди ведущий ноль
                    day = day.zfill(2)
                    month = month.zfill(2)

                    # Записываем дату в ISO формате
                    birthday_iso = f"{year}-{month}-{day}"
                else:
                    birthday_iso = 'Unknown'

                # Получаем из списка SEX строковое значение пола
                sex = SEX[friend.get('sex')]

                writer.writerow({
                    'first_name': first_name, 'last_name': last_name,
                    'country': country, 'city': city,
                    'birth_date': birthday_iso, 'sex': sex
                    })
    except PermissionError:
        print(f'Закройте файл {filename}_{file_number} перед началом сбора данных!')
        quit()
    except FileNotFoundError:
        print('Указан не существующий путь. Проверьте сущеcтвует ли введёный путь.')
        quit()


def write_tsv(path, friends, filename, first_request, file_number):

    # Название столбцов
    fieldnames = ['first_name', 'last_name', 'country', 'city', 'birth_date', 'sex']

    try:

        # Если это первая запись в файл, то записываем заголовок(название столбцов)
        if first_request:
            with open(f'{path}/{filename}_{file_number}.tsv', 'w', encoding='utf-8') as file:
                writer = csv.DictWriter(file, delimiter='\t', fieldnames=fieldnames, lineterminator='\n')
                writer.writeheader()

        with open(f'{path}/{filename}_{file_number}.tsv', 'a', encoding='utf-8') as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=fieldnames, lineterminator='\n')

            # Распарсиваем данные о каждом друге
            # Если какого то из полей 'country', 'city' или  'bdate' нету
            # то присваиваем им значение 'Unknown'
            for friend in friends:
                first_name = friend['first_name']
                last_name = friend['last_name']

                if 'country' in friend:
                    country = friend.get('country').get('title')
                else:
                    country = 'Unknown'

                if 'city' in friend:
                    city = friend.get('city').get('title')
                else:
                    city = 'Unknown'

                if 'bdate' in friend:
                    birthday = friend.get('bdate')

                    # Разделяем строку даты на элементы, чтобы узнать имеется ли год,
                    # если год имеется, то количество элементов будет равным 3
                    elements_count = birthday.split('.')

                    # Если год отсутствует, то прибавляем в строку значение 'YYYY',
                    # т.к. нам неизвестно какого года рождения друг
                    if len(elements_count) < 3:
                        birthday += '.YYYY'
                    day, month, year = birthday.split('.')

                    # ISO формат имеет вид YYYY-MM-DD
                    # поэтому если месяц или дата меньше 10, то добавляем спереди ведущий ноль
                    day = day.zfill(2)
                    month = month.zfill(2)

                    # Записываем дату в ISO формате
                    birthday_iso = f"{year}-{month}-{day}"
                else:
                    birthday_iso = 'Unknown'

                # Получаем из списка SEX строковое значение пола
                sex = SEX[friend.get('sex')]

                writer.writerow({
                    'first_name': first_name, 'last_name': last_name,
                    'country': country, 'city': city,
                    'birth_date': birthday_iso, 'sex': sex
                })
    except PermissionError:
        print(f'Закройте файл {filename}_{file_number} перед началом сбора данных!')
        quit()
    except FileNotFoundError:
        print('Указан не существующий путь. Проверьте сущеcтвует ли введёный путь.')
        quit()


dict = {'friends': []}


def write_json(path, friends, filename):
    try:
        with open(f'{path}/{filename}.json', 'w', encoding='utf-8') as file:

            # Распарсиваем данные о каждом друге
            # Если какого то из полей 'country', 'city' или  'bdate' нету
            # то присваиваем им значение 'Unknown'
            for friend in friends:
                first_name = friend['first_name']
                last_name = friend['last_name']

                if 'country' in friend:
                    country = friend.get('country').get('title')
                else:
                    country = 'Unknown'

                if 'city' in friend:
                    city = friend.get('city').get('title')
                else:
                    city = 'Unknown'

                if 'bdate' in friend:
                    birthday = friend.get('bdate')

                    # Разделяем строку даты на элементы, чтобы узнать имеется ли год,
                    # если год имеется, то количество элементов будет равным 3
                    elements_count = birthday.split('.')

                    # Если год отсутствует, то прибавляем в строку значение 'YYYY',
                    # т.к. нам неизвестно какого года рождения друг
                    if len(elements_count) < 3:
                        birthday += '.YYYY'
                    day, month, year = birthday.split('.')

                    # ISO формат имеет вид YYYY-MM-DD
                    # поэтому если месяц или дата меньше 10, то добавляем спереди ведущий ноль
                    day = day.zfill(2)
                    month = month.zfill(2)

                    # Записываем дату в ISO формате
                    birthday_iso = f"{year}-{month}-{day}"
                else:
                    birthday_iso = 'Unknown'

                # Получаем из списка SEX строковое значение пола
                sex = SEX[friend.get('sex')]

                # Собираем словарь данных друга
                friend_dict = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'country': country,
                    'city': city,
                    'birth_date': birthday_iso,
                    'sex': sex
                }

                # Добавляем данные в список
                dict['friends'].append(friend_dict)
            json.dump(dict, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print('Указан не существующий путь. Проверьте сущеcтвует ли введёный путь.')
        quit()
