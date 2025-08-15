<h2>Автотесты на API проекта «Битва покемонов» с помощью Pytest и Requests</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизированы
* Создание покемона `POST /pokemons`
* Переименование покемона `PUT /pokemons`
* Поимка покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит поле `trainer_name`

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests

<img width=500px src="1.png"/>

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
3. Выполнить команду:

Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для Windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Устанавливаем библиотеки

``` markdown
python3 -m pip install requests
```

``` markdown
python3 -m pip install pytest
```

Запускаем
``` markdown
pytest tests/test_pokemon.py
```

5. Ожидаемый результат: получим отчет о прохождении тестов.
