from collections import defaultdict
from aocd import get_data, submit

data = (get_data(day=1, year=2023))
#submit(answer=ans, part=2, day=1, year=2023)

data = data.splitlines()
mapDigits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9}
mnapkeys = mapDigits.keys()
d1 = []
for line in data:
    numbers = []
    lineCopy = line
    for k in mapDigits:
        lineCopy = lineCopy.replace(k, str(k[0]) + str(mapDigits[k])+ str(k[-1]))
    print(lineCopy)
    for l in lineCopy:
        if l.isnumeric():
            y  = l
            numbers.append(y)
    print(numbers[0], numbers[-1])
    d1.append(numbers)

xd = [int("".join([d[0], d[-1]])) for d in d1]

print(xd)
print(sum(xd))
ans = sum(xd)
#data = [sum(d) for d in data]
#ans = max(data)
#data = data.replace("\n", "")
#data = list(map(lambda x: x, data))
print(ans)

#submit(answer=ans, part=2, day=1, year=2023)
