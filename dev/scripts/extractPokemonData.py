import requests
import json
csvLines = []
api_endpoint = 'https://pokeapi.co/api/v2/pokemon/'
with open('{{ workingDir }}/pokemons.json') as f:
    pokemons = json.load(f)
for pokemon in pokemons:
    fields = {}
    response = requests.get(api_endpoint + pokemon)
    data = json.loads(response.text)
    fields['name'] = data['name']
    csvLines.append(fields)
print(csvLines)