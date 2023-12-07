from collections import defaultdict
from aocd import get_data, submit
import re
import numpy as np
from utils.aocutils import *
data = get_data(day=3, year=2023)
#data = open("day3/test.txt", "r").read()

data = data.splitlines()
matrix = []
for d in data:
    matrix.append(d.strip())

matCopy = matrix.copy()
total_sum = 0

#Part 1 loop
pattern = r"\d+"
for rx, row in enumerate(matrix):
    numbers = re.finditer(pattern, matCopy[rx])
    for num in numbers:
        found = False
        indexSpan = range(num.start(), num.end())
        number = num.group()
        for x in indexSpan:
            neighbours = get_neighbors_with_diagonal(row = rx, col = x, grid=matrix)
            for n in neighbours:
                symbol = re.findall(r"[^\d.]", matrix[n[0]][n[1]])
                if symbol:
                    total_sum += int(number)
                    found = True
                    break
            if found:
                break

print(total_sum)


#Part 2 loop
pattern = r"\d+"
gears = defaultdict(list)
for rx, row in enumerate(matrix):
    numbers = re.finditer(pattern, matCopy[rx])
    for num in numbers:
        found = False
        indexSpan = range(num.start(), num.end())
        number = int(num.group())
        for x in indexSpan:
            neighbours = get_neighbors_with_diagonal(row = rx, col = x, grid=matrix)
            for n in neighbours:
                symbol = re.findall(r"\*", matrix[n[0]][n[1]])
                if symbol:
                    gears[n].append(number)
                    found = True
                    break
            if found:
                break

tot_sum = 0
for key, value in gears.items():
    if len(value) == 2:
        tot_sum += (value[0]*value[1])
print(tot_sum)
