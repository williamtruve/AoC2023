import re
from aocd import get_data

data = get_data(day=1, year=2022)
#https://www.kdnuggets.com/2023/08/mastering-regular-expressions-python.html
# Define a pattern
print(data)
#aiLmsux
pattern = r"\n{2}(\d+\n)+\n{1}"
# Search for the pattern

# Search for the pattern
matches = re.findall(pattern, data)
print()
matches = re.finditer(pattern, data)
for it in matches:
    print(ma)
print("matches = ", matches)
