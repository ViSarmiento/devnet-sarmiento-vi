# Module 1 — Git & GitHub


**Student:** [Sarmiento, John Vincent S.]
**Date:** [Sept. 26, 2026]


---


## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)


[Okay so imagine you're playing Pokemon and you want to keep every save file before a big gym battle or the Champion Fight, in case you mess up. Git is like a save system that remembers every single change you make to your team, your items, your progress. It also lets you jump back in time to any save file you made. It lives on your console/computer, No internet needed.


GitHub is like the Pokemon Wonder Trade or the Trade station thing inside the Pokemon Center. It's a website/tool where you upload those save files so friends can see them, trade ideas, or test your code together. Git is the save system. GitHub is the place you share the saves.]


---


## Key vocabulary (in your own words)


- repository: PC storage box in pokemon. A project folder that Git tracks
- commit: Save point, can also add messeges for future references, for sample "I just beat the eliute 4, I need to save before the champion fight"
- branch: I think of it as another timeline after i soft reset from a save point, like picking bulbasaur instead of charmander when i first get the choice of starters, but the timeline where i picked charmander is still there
- push / pull: push is for uploading to GitHub, pull is for downloading someone else's save to your cartridge/console
- pull request: request for merging works
- merge conflict: imagine two trainers edit the same Pikachu's moveset at the same time, Git won't know what version to keep so it makes you pick


---


## Walking through what I did


[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]
[I made this branch for module 1, then edit the notes.md, i git added and committed as well then pushed.]


```
# git branch mod1
git checkout mod1
git add .
git commit -m "made branch por mod1 and edited notes.md"
git push -u origin mod1
```


---


## A mistake I made (or one I want to avoid)


[I git added the notes.md but it's not working then i researched and found out that i have to use the path isntead, if a command isn't working, don't just keep spamming it. Look it up. Read the error. Nine times out of ten the answer is right there and you just feel silly afterward (in a good way)]


---


## How this connects to something else


[Optional: how does version control relate to anything else you've learned or used before?]
