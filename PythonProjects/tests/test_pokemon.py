import requests
import pytest

host= 'https://api.pokemonbattle.me/v2'

def test_check_response():
    response = requests.get(f'{host}/trainers',params= {'trainer_id':2657})
    assert response.json()['data'][0]
    ['trainer_name'] == 'Chaplin' 
    
    
 
def test_status_code_200():
    response = requests.get(url = f'{host}/trainers' , params = { 'trainer_id': 2657})
    assert response.status_code == 200