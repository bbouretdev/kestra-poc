import requests
      import json
      pokemons = []
      api_endpoint = 'https://pokeapi.co/api/v2/pokemon/'
      response = requests.get(api_endpoint)
      if response.status_code == 200:
          data = json.loads(response.text)
          nextCall = data['next']
          print("Next call URL:", nextCall)
          for i in data['results']:
              pokemons.append(i['name'])
      else:
          print("Error:", response.status_code, response.text)
      print(nextCall)
      print(pokemons)
      with open('{{ outputDir }}/pokemons.json', 'w') as f:
          json.dump(pokemons, f)
      print('{{ outputDir }}')