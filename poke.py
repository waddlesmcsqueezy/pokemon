import requests
import json

api_url = "https://pokeapi.co/api/v2/pokemon"

poke_count = 3

attribute = "name"

responses = {}

id = 1

#n = requests.get("%s/%s" % (api_url, str(1)))
#data = n.json()
#print(data[attribute])
while id <= poke_count:
	responses[str(id)] = (requests.get("%s/%s" % (api_url, str(id))).json())
	id += 1

with open('data.txt', 'w') as outfile:
    json.dump(responses, outfile)