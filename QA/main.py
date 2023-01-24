import requests
import json

token = '9db5fe966ce95921565608b5a34853d0'


response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json',
 'trainer_token': token},
json = {
    "name": "zalip",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
}) 
print(json.dumps(response.json(), indent = 2))


response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json',
 'trainer_token': token}, json = {
     "pokemon_id": 3324,
    "name": "Zalipchik",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
 })
print(json.dumps(response_change.json(), indent = 4))


response_add_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type': 'application/json',
'trainer_token': token},
json = {
    "pokemon_id": "3326"
})
print(json.dumps(response_add_pokeball.json(), indent = 4))