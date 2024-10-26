## Проект API:

### Описание

_Проект API сервиса Yatube-api. Предназначен для взаимодествия устройств
с бэкэнд частью сайта расположенном на сервере. Помогает в создании общего
доступа для разных устройств. Позволяет получать и передовать данные с разных 
носителей. Обеспечивает разные безопасные механизмы работы для авторизованных и
не авторизованных пользователей на сайте. Этот механизма отвечает за логику создания,
просмотра постов, сообщений и подписок._



### Как запустить проект


Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Перейдите в папку с файлом manage.py и Запустите проект:

```
python manage.py runserver
```

### Примеры запросов к API



GET-запрос. Получение всех постов автора 

```
/api/v1/posts/
```

Ответ Response

```
{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

[

        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]

}
```

Post - запрос.  Создание публикации

```
/api/v1/posts/
```
Образец запроса

```
{

    "text": "string",
    "image": "string",
    "group": 0

}
```
Ответ Response

```
{

    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0

}
```

Get - запрос. Получение информации о Подписках пользователя

```
/api/v1/follow/
```

Ответ Response

```
[

    {
        "user": "string",
        "following": "string"
    }

]
```

Post - запрос. Создание Подписки на пользователя

```
/api/v1/follow/
```

Образец запроса

```
{

    "following": "string"

}
```
Ответ Response

```
{

    "user": "string",
    "following": "string"

}
```