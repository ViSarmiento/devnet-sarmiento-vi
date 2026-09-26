"""
Module 2 — Lesson 1: Variables & Data Types
Student: [Sarmiento, John Vincent S.]
Date: [9/26/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Think of variables like Pokémon Trainer stats. You give each one a name (like trainer_name) and put a value inside it ("Ash"). That's it — a labeled box holding one piece of info.

Data types are just what kind of thing is inside the box:

A number like your badge count → int

A number with decimals like your Pokémon's weight → float

Text like your rival's name → string

A yes/no like "is Pikachu evolved?" → boolean

Python figures out the type automatically when you assign it.]


============================================
KEY VOCABULARY
============================================
- variable: A named box that stores one value. Like a Poké Ball holding one Pokémon.
- data type: What kind of value is inside — number, text, true/false.
- int: A whole number.
- float: A number with a decimal.
- string: Text in quotes.
- boolean: Only True or False. Like a yes/no switch.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

trainer_name = "Vi"         # string
badges = 8                   # int
umbreon_weight = 59.5         # float
has_evolved = True          # boolean

print(trainer_name, "has", badges, "badges.")
print("Umbreon weight:", umbreon_weight)
print("Evolved?", has_evolved)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I forgot quotes around text once — name = Umbreon 
and Python thought Pikachu was a variable that didn't exist. 
Error: NameError. Always put text in quotes. Numbers don't need them.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
