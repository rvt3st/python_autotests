import requests
import pytest

host = 'https://api.pokemonbattle.ru/v2'
token = 'USER_TOKEN'
headers = {'Content-Type' : 'application/json', 'trainer_token' : token}

# 1. Создание покемона

body_create = {
	"name": "Pikachu",
	"photo_id": 25
}

response_create = requests.post(url = f'{host}/pokemons', headers = headers, json = body_create)
if response_create.status_code == 201:
    pokemon_id = response_create.json()["id"]
    print('Покемон создан с ID ' + pokemon_id)
else:
    print('Ошибка при создании покемона: ' + response_create.json()['message'])
    exit()

# 2. Переименование покемона

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Пикачу"
}

response_rename = requests.patch(url = f'{host}/pokemons', headers = headers, json = body_rename)
if response_rename.status_code == 200:
    print('Покемон с ID ' + pokemon_id + ' переименован в Пикачу')
else:
    print('Ошибка при переименовании покемона: ' + response_rename.json()['message'])

# 3. Поимка покемона в покебол

body_addPokeball = {
    "pokemon_id": pokemon_id
}

response_addPokeball = requests.post(url = f'{host}/trainers/add_pokeball', headers = headers, json = body_addPokeball)
if response_addPokeball.status_code == 200:
    print('Покемон с ID ' + pokemon_id + ' пойман в покебол')
else:
    print('Ошибка при поимке покемона в покебол: ' + response_addPokeball.json()['message'])