import requests
import pytest

host = 'https://api.pokemonbattle.ru/v2'
token = 'USER_TOKEN'
headers = {'Content-Type' : 'application/json', 'trainer_token' : token}
trainer_id = 38235

# 1. Проверка, что ответ запрос GET /trainers приходит с кодом 200

def test_status_code():
	response = requests.get(url = f'{host}/trainers')
	assert response.status_code == 200
	

# 2. Проверка, что в ответе на запрос по конкретному тренеру приходит строчка с именем
	
def test_trainerName():
	response_trainer = requests.get(url = f'{host}/trainers', params = {'trainer_id' : trainer_id})
	assert "trainer_name" in response_trainer.json()["data"][0]
