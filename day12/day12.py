import enum
import functools
import itertools
from turtle import pos
import more_itertools
from aocd import get_data, submit
from collections import Counter
import math
import networkx as nx
from pyparsing import col
from sympy import memoize_property, true
from tqdm import tqdm
import numpy as np
import regex as re
from utils.aocutils import get_neighbors
import multiprocessing
import copy

def solve(records: str, groups: tuple) -> int:
    if len(groups) == 0:  # base case
        no_broken_springs_remaining = '#' not in records
        return 1 if no_broken_springs_remaining else 0
    pipesToPlace = groups[0]

    group_min_start = 0
    group_max_start = len(records) - sum(groups) - len(groups) + 1

    if '#' in records:  # cannot start first damaged spring
        group_max_start = min(records.index('#'), group_max_start)
    arrangements = 0

    for ix in range(group_min_start, group_max_start + 1):  # sliding window
        group = records[ix: ix + pipesToPlace]
        is_group_possible = all(char in '#?' for char in group)
        is_end_of_record = ix+pipesToPlace >= len(records)
        is_group_separated = is_end_of_record or records[ix+pipesToPlace] in '.?'
        if not is_group_possible or not is_group_separated:
            continue
        
        remaining_record = records[ix+pipesToPlace+1:]
        remaining_groups = groups[1:]
        arguments = [remaining_record, remaining_groups]
        arrangements += solve(*arguments)
    return arrangements

if __name__ == "__main__":
    data = get_data(day=12, year=2023).splitlines()
    record_sum = 0
    for d in data:
        records, groups = d.split(" ")
        group_sizes = list(map(int, groups.split(",")))*5
        recordp2 = copy.deepcopy(records)
        for _ in range(4):
            recordp2 += "?" + records
        record_sum += solve(recordp2, tuple(group_sizes))
    print(record_sum)