from aocd import get_data
import more_itertools
import itertools
import functools
data = get_data(day=9, year=2023).splitlines()
def recursion(list_of_numbers):
    diff = list(more_itertools.difference(list_of_numbers, initial=0))
    if any(diff):
        return diff[-1] + recursion(diff)
    return 0
def solve(data, reverse = False):
    total_sum = 0
    for row in data:
        dx = list(reversed([int(d) for d in  row.split()])) if reverse else (([int(d) for d in  row.split()]))
        total_sum += dx[-1]+ + recursion(dx)
    print(total_sum)
solve(data)
solve(data, True)
