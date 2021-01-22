#!/usr/bin/env python3

birds = {}
bird_seen = ""

# Voting
while bird_seen != "N":
    bird_seen = input("Enter a bird you saw: ")
    if bird_seen == "N":
        break
    try: # <-- if bird_seen in birds
        birds[bird_seen] += 1
    except KeyError: # <-- The key is not there; aka "else"
        birds[bird_seen] = 1

# Counting

max_bird = 0
bird_type = ""

for bird in birds:
    # Pull out the count 
    count = birds[bird]
    if count > max_bird:
        max_bird = count
        bird_type = bird
    # Print out each bird and count
    print("I saw",count,bird + "s")

print(f"The bird I saw the most of was a {bird_type}; I saw {max_bird} of them.")