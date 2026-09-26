"""
Module 2 — Lesson 3: Loops & Lists
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[A list is like your Pokémon party — one container holding several things in order. ["Garchomp", "Dragonite", "Baxcalibur"] is a party of three.

A loop is what you do when you want to act on every member of your party without writing the same line 6 times. 

Instead of "heal Garchomp, heal Dragonite, heal Baxcalibur...", you say "heal each Pokémon in my party." That's a for loop.

A while loop is different — it keeps going as long as a condition is true. Like "keep attacking while enemy HP > 0."

]


============================================
KEY VOCABULARY
============================================
- list: An ordered container of items. 
- for loop: Goes through every item in a list once. "For each Pokémon in my party..."
- while loop: Repeats while a condition stays true. Like a battle turn loop.
- index: The position number of an item. Starts at 0. party[0] is the first Pokémon.
- iteration: One single pass through the loop. One turn.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
party = ["Garchomp", "Dragonite", "Baxcalibur"]

for pokemon in party:
    print(pokemon, "is ready to battle!")

print("First in party:", party[0])   # index 0

hp = 3
while hp > 0:
    print("Enemy HP:", hp)
    hp = hp - 1
print("Enemy fainted!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I thought back then that [1] was the first value. 
Nope — indexes start at 0. 
So in this case party[0] is Garchomp, party[1] is Dragonite. 
Off-by-one errors are like miscounting your badges — small mistake, big confusion.
Also, a while loop without any changes inside is an infinite loop, it will keep running
always add break or and else condition so that code can stop]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
