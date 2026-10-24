import requests
import random

Pokemon_List = ["umbreon", "espeon", "sceptile", "haxorus", "baxcalibur"]
answer = random.choice(Pokemon_List)

try:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{answer}")
except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")
    exit()

Pokemon = response.json()
name = Pokemon.get('name')
height = Pokemon.get('height')
weight = Pokemon.get('weight')

abilities = []
for item in Pokemon['abilities']:
    abilities.append(item['ability']['name'])
abilities_text = ", ".join(abilities)

print("Who's that Pokemon??")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Abilities: {abilities_text}")

for attempt in range(1, 4):
    guess = input(f"Attempt {attempt}/3 - Your guess: ").strip().lower()
    if guess == name:
        print(f"Correct! It's {name.capitalize()}!")
        break
    print("Wrong! Try Again!")
else: 
    print(f"Game Over! The Pokemon is {name.capitalize()}.")