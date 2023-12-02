from collections import defaultdict
from aocd import get_data, submit

file = open("inp.txt", "r").read().splitlines()#submit(answer=ans, part=2, day=1, year=2023)

data = file
print(data)
total_sum = 0
for ix, input in enumerate(data):
    data = input.split(":")[-1]
    data = "".join(data).split(";")
    maxDict = {"red": 0, "green": 0, "blue": 0}
    for round in data:
        for value in round.split(","):
            valueColor = (value.strip().replace(" ", "=")).split("=")
            color = valueColor[-1]
            number = int(valueColor[0])
            if maxDict[color] < number:
                maxDict[color] = number
    power = maxDict["blue"]*maxDict["green"]*maxDict["red"]
    print(power)
    total_sum += power
print(total_sum)