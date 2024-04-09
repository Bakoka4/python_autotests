import requests

token = "832767a7df2e0fc227f08d06c890fffb"

response = requests.post("https://api.pokemonbattle.me/v2/pokemons", json= {
    "name": "ChapliN",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
    }, headers= {"trainer_token":token,
                 "Content-Type":"application/json"})

print(response.text)

response = requests.put("https://api.pokemonbattle.me/v2/pokemons", json= {
    "name": "Fixik",
    "pokemon_id": "17018",
    "photo": "https://dolnikov.ru/pokemons/albums/057.png"
    }, headers= {"trainer_token": token,
                 "Content-Type":"application/json"})

print(response.text)

response = requests.post("https://api.pokemonbattle.me/v2/trainers/add_pokeball", json= {
    "pokemon_id": "17018"
    }, headers= {"trainer_token": token,
                 "Content-Type":"application/json"})

print(response.text)