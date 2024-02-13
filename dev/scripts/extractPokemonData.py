import requests
import json
csvLines = []
api_endpoint = 'https://pokeapi.co/api/v2/pokemon/'
with open('pokemons.json') as f:
    pokemons = json.load(f)
for pokemon in pokemons:
    fields = {}
    response = requests.get(api_endpoint + pokemon)
    data = json.loads(response.text)
    fields['name'] = data['name']
    fields['hp'] = data['stats'][0]['base_stat']
    fields['attack'] = data['stats'][1]['base_stat']
    fields['defense'] = data['stats'][2]['base_stat']
    fields['spa'] = data['stats'][3]['base_stat']
    fields['spd'] = data['stats'][4]['base_stat']
    fields['spe'] = data['stats'][5]['base_stat']
    csvLines.append(fields)
print(csvLines)