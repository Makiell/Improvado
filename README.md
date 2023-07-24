<h1 align="center">Improvado Back-end task</h1>


[![VK](https://img.shields.io/badge/-VK-0080B5?logo=vk&logoColor=&style=for-the-badge)](https://vk.com/)

**`Программа позволяющая получить список друзей из ВКонтакте`**


# Установка библиотек
    Для установки всех библиотек выполните данную команду:
    
    pip install -r requirements.txt

# Авторизация
    Для работы программы необходимо получить токен.
    1. Перейдите на сайт 
**[dev.vk.com](https://dev.vk.com/)**

    2. Нажмите кнопку "Управление"
![Image-alt](https://github.com/Makiell/Improvado/blob/main/images/2.png)

    3. Нажмите кнопку создать, дайте название вашему приложение и выберите Standalone-приложение
![Image alt](https://github.com/makiell/improvado/blob/main/images/3.png)

    4. Далее в левом меню перейдите в настройки
![Image alt](https://github.com/makiell/improvado/blob/main/images/4.png)

    Перед вами будут настройки вашего созданного приложения, поменяйте настройку "Состояние" в "Приложение включено и видно всем"
    Нажмите на иконку глаза в поле "Сервисный ключ доступа" и скопируйте данный токен
    это и есть ваш авторизационный токен
![Image alt](https://github.com/makiell/improvado/blob/main/images/5.png)

    Данный токен надо будет вводить при запуске программы в данном поле:
![Image alt](https://github.com/makiell/improvado/blob/main/images/6.png)

# Как запустить программу

    После установки всех необходимых библиотек выполните данную команду:
    python main.py

# Задействованные эндпоинты

* **friends.get** - *Возвращает список идентификаторов друзей пользователя или расширенную информацию о друзьях пользователя*

* **users.get** - *Возвращает расширенную информацию о пользователях*

# Как работает скрипт

    С помощью VK API программа получает список друзей пользователя с определённым ID (user_id)
    
    Метод friends.get в программе используется для того чтобы получить список айдишников друзей
    А метод users.get с помощью полученных айдишников друзей возвращает расширенную информацию о каждом друге
    
    С целью оптимизации кода и предотвращения нехватки оперативной памяти программа получает список друзей частями 
    и записывает их в файл, далее получает новый список друзей и так же записывает их в файл

    Во время выполнения программы присутствуют подсказки по которым можно отследить состояние скрипта

    Так же в файлах присутствуют подробные комментарии которые объясняют код
