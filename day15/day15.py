import errno
import itertools
from operator import index
from re import X
import more_itertools
from aocd import get_data, submit
from collections import Counter, deque
import math
import networkx as nx
from pyparsing import col
from sympy import true
from tqdm import tqdm
import numpy as np
import regex as re
from utils.aocutils import get_neighbors
import multiprocessing
import functools
from collections import defaultdict

def getNum(string) -> int:
    curVal = 0
    for char in string:
        curVal += ord(char)
        curVal *= 17
        curVal = curVal % 256
    return curVal

if __name__ == "__main__":
    data = open("day15/input.txt", "r").read().split(",")
    lensesInBox = defaultdict(list)
    #data = open("day15/test.txt", "r").read().split(",")
    focalLengthOfHash = defaultdict(int)
    pattern = r"(?P<boxHash>\w+)(?P<operation>[-=])(?P<vocalLength>\d*)" #Extract box hash, operation = or -, and finally if there is a vocal length extract that as well
    for hash in data:
        match = re.search(pattern, hash.strip())
        if match:
            boxHash = match['boxHash']
            operation = match['operation']
            boxNumber = getNum(boxHash)
            if operation == "=":
                vocalLength = match['vocalLength']
                focalLengthOfHash[boxHash] = int(vocalLength)
                if not boxHash in lensesInBox[boxNumber]:
                    lensesInBox[boxNumber].append(boxHash)
                else:
                    continue
            elif boxHash in lensesInBox[boxNumber]:
                        lensesInBox[boxNumber].remove(boxHash)
        else:
            raise Exception(f"could not match on hash {hash}")
    fullSum = 0
    for key, val in lensesInBox.items():
        boxNumber = key + 1
        for slotpos, v in enumerate(val):
            fullSum += boxNumber * (slotpos+1) * int(focalLengthOfHash[v])
    print(fullSum)

    