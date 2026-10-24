import requests
import random

Pokemon_List = [umbreon, espeon, sceptile, haxorus, baxcalibur]
name = random.choice(Pokemon_List)

response = requests.get('https://pokeapi.co/api/v2/pokemon/gengar')
Pokemon = response.json()


height = Pokemon.get('height')
weight = Pokemon.get('weight')

print("Who's that Pokemon??")
print(height)
print(weight)