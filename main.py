import os

import vk_api
from write_to_file import write_csv, write_json, write_tsv


def get_more_friends(user_id, session, offset):

    count = 500

    # Т.к. API VK не даёт возможность получить информацию больше чем о 5000 друзей,
    # сначала получаем список айдишников друзей и далее передаём их в метод users.get для подробной информации
    # P.S в данном запросе нельзя использовать поле 'fields' т.к. не сможем получить больше 5000 друзей
    id_list = session.method('friends.get', {
        'user_id': user_id,
        'order': 'name',
        'offset': offset,
        'count': count,
    })['items']

    # Метод users.get для получения информации о друзьях в поле 'user_ids' принимает строку из айдишников
    # разделённых запятой, поэтому из списка айдишников делаем строку
    id_str = ''
    for id in id_list:
        id_str += str(id) + ','

    # Здесь получаем подробную информацию о каждом друге
    friends = session.method('users.get', {
        'user_ids': id_str,
        'fields': 'bdate,country,city,sex'
    })
    return friends


def main():

    print('Вы находитесь в начале этапа сбора данных друзей\n')
    token = input('Введите свой авторизационный токен: ')

    session = vk_api.VkApi(token=token)  # 6482496864824968648249684c67974fdc66482648249680038d0935cb27a3f2d295ec2

    user_id = input('Введите ID пользователя: ')

    # Сразу проверяем правильность ввода токена и ID, при ошибке выводем сообщение
    try:
        # friends_check это переменная для того чтобы знать сколько друзей у данного пользователя,
        # т.к. API VK не позволяет получить информацию о более чем 5000 друзей при использовании поля "fields"
        # данное поле здесь не используется
        friends_check = session.method('friends.get', {
            'user_id': user_id,
            'order': 'name',
            'count': 1
        })
    except vk_api.exceptions.VkApiError as e:
        print("\n"+str(e))
        return

    path = input(f'Введите путь для сохранения файла (Default: {os.getcwd()}): ')

    # Если путь не введён, то сохраняем в переменную path текущую директорию
    if not path:
        path = os.getcwd()

    filename = input('Введите название файла (Default: report): ')

    if not filename:
        filename = 'report'

    format = input('Введите формат файла (csv, tsv, json) (Default: csv): ')
    formats = ['csv', 'tsv', 'json']

    if not format:
        format = 'csv'

    # Если пользователь ввёл неверный формат то выводим сообщение об этом
    if format not in formats:
        print('\nВы ввели неверный формат файла!\nДоступны следующие форматы файлов:\n')
        for i in formats:
            print('\t' + i)
        print('\nВыберите любой из вышеперечисленных форматов для работы программы.')
        quit()

    offset = 0  # Переменная обозначающая отступ при запросе через API для получения друзей
    first_request = True  # Переменная необходимая для того чтобы при первой записи в файл создавались имена столбцов
    file_number = 1  # Пагинация, все данные распределяются в два файла, максимум по 5000 записей в каждой,
                    # т.к максимальное количество друзей в ВК 10.000

    print(f'\nЗагрузка...\nВыполняется выгрузка списка друзей в файл\nПуть: {path}\{filename}.{format}\n')

    # Цикл с помощью которого программа по частям получает друзей пользователя, по 500 друзей
    # после каждого выполнения отступ увеличивается на 500 и программа получает следующих 500 друзей
    # сделано это для оптимизации кода а так же чтобы не упереться в оперативную память
    # запись в файлы происходит так же по 500 записей
    while offset <= friends_check['count']:

        friends = get_more_friends(session=session, user_id=user_id, offset=offset)  # Получаем по 500 друзей

        if format == 'csv':
            write_csv(path, friends, filename, first_request, file_number)
        if format == 'tsv':
            write_tsv(path, friends, filename, first_request, file_number)
        if format == 'json':
            write_json(path, friends, filename)

        offset += 500

        print(f'Собираем первых {offset} друзей')

        # Если отступ равняется 5000 то создаём новый файл для записи
        if offset == 5000:
            print(f'\nИнформация о {offset} друзьях записана в файл {filename}_{file_number}.{format}')
            file_number += 1
            print(f'Создаем новый файл {filename}_{file_number}.{format}\n')
            first_request = True  # Переключаем переменную т.к. мы будем создавать новый файл, и это будет первая запись
        else:
            first_request = False

    print(f'\nВыгрузка списка друзей окончена!\nБыла записана информация о {friends_check["count"]} друзьях')


if __name__ == '__main__':
    main()
