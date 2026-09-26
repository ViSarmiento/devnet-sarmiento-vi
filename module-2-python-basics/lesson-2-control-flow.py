"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Control flow is like a Pokémon battle sequence. 
The game checks a condition, then picks one path. 
"Is enemy HP below 0? If yes → they faint. Else if it's below half → I should heal. Else → keep attacking."

if = first check. 
elif = "okay, but what if instead...". 
else = catch-all when nothing else matched. 
Python runs only one branch, top to bottom — like picking exactly one move per turn.]


============================================
KEY VOCABULARY
============================================
- condition: A yes/no question. Like "Is Pikachu's level above 50?"
- if / elif / else: The decision branches. if is first, elif is extra checks, else is the fallback.
- comparison operator: Symbols that compare two things
- boolean expression: Any question that gives True or False. "Fire > Grass" → True.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
hp = 45
max_hp = 100

if hp <= 0:
    print("Your Pokémon fainted!")
elif hp < max_hp / 2:
    print("HP is low — use a Potion!")
else:
    print("HP is fine, keep battling!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[Back then I used = instead of == inside an if. 
= assigns, == compares. Python gave me a SyntaxError. 
It's like trying to throw a Poké Ball by eating it
right item, wrong action. Always use == when comparing]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
