import requests
import json
import pandas as pd 
from sqlalchemy import create_engine

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
df = pd.DataFrame(csvLines)
host = "localhost"
port = "5431"
database = "kestra-poc"
user = "kestra"
password = "kestra"
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
# Write into Postgre table
df.to_sql("pokemons", engine, if_exists="append", index=False)
# Write dataframe into output CSV file
df.to_csv("pokemons.csv", index = False)