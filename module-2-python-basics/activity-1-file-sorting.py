"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Sarmiento, John Vincent S.]
Date: [09/26/2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Imagine your PC folder is a messy Pokémon bag, Potions mixed with Poké Balls, TMs everywhere, no order. 
My script is like a automatic Bag Sorter: it looks at each file, checks its type, and 
drops it into the right pocket — images in one folder, documents in another]


============================================
KEY VOCABULARY
============================================
- os module: The tool that lets Python talk to your computer's folders — like checking what's inside your Bag
- shutil module: The tool that moves the files, like physically relocating a Pokémon to a different box.
- file path: The address of a file. Like "Route 1 -> Viridian City d-> Poké Mart."
- directory: A folder. A storage box for your files.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
source_folder = os.path.join(script_dir, "my_files")

images_folder = os.path.join(source_folder, "Images")
docs_folder   = os.path.join(source_folder, "Documents")
others_folder = os.path.join(source_folder, "Others")

if not os.path.exists(source_folder):
    print(f"Target directory '{source_folder}' does not exist.")
else:
    for folder in [images_folder, docs_folder, others_folder]:
        os.makedirs(folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if not os.path.isfile(file_path):
            continue

        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            shutil.move(file_path, os.path.join(images_folder, filename))
            print(f"Moved {filename} -> Images/")
        elif filename.lower().endswith((".pdf", ".docx", ".txt")):
            shutil.move(file_path, os.path.join(docs_folder, filename))
            print(f"Moved {filename} -> Documents/")
        else:
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved {filename} -> Others/")

    print("Done sorting!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I ran the script but my_files didn't exist yet, so it crashed. 
added if not os.path.exists(source_folder) check first to print a friendly message instead.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
