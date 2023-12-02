from collections import defaultdict
from aocd import get_data, submit

file = open("inp.txt", "r").read().splitlines()
data = file

red = 12
green = 13
blue = 14

total_sum = 0
for ix, game in enumerate(data):
    data = game.split(":")[-1]
    data = "".join(data).split(";")
    invalid_game = False

    for round in data:
        for value in round.split(","):
            invalid_game = eval(value.strip().replace(" ", ">"))
            if invalid_game:
                break
        else:
            continue
        break
    if invalid_game == False:
        print(ix+1)
        total_sum += (ix+1)  
print(total_sum)

#submit(answer=ans, part=2, day=1, year=2023)
