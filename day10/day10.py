
import functools
import itertools
from operator import indexOf
import matplotlib.pyplot as plt
import more_itertools
from aocd import get_data, submit
from collections import Counter
import math
import networkx as nx
from pyparsing import col
from sympy import true
from tqdm import tqdm
import numpy as np

def get_neighbors_easy(rc, grid):
    row, col = rc
    symbol = grid[row][col]
    up = []
    left = []
    right = []
    down = []
    neighbors = []

    if row > 0:
        up = ((row - 1, col))  # Up
    if col < len(grid[0]) - 1:
        right = ((row, col + 1))  # Right
    if row < len(grid) - 1:
        down = ((row + 1, col))  # Down
    if col > 0:
        left = ((row, col - 1))  # Left

    if symbol == "|":
        neighbors = [up, down]

    elif symbol == "-":
        neighbors = [left, right]

    
    elif symbol == "L":
        neighbors = [up, right]


    elif symbol == "J":
        neighbors = [left, up]

    elif symbol == "7":
        neighbors = [left, down]

    elif symbol == "F":
        neighbors = [down, right]
    elif symbol == ".":
        neighbors = []
    elif symbol == "S":
        neighbors = [up, down, left, right]
    return neighbors

def gs(grid, rc):
    row, col = rc
    symbol = grid[row][col]
    return (symbol, rc)
def get_neighbors(rc, grid):
    row, col = rc
    symbol = grid[row][col]

    up = []
    left = []
    right = []
    down = []
    neighbors = []
    if row > 0:
        up = ((row - 1, col))  # Up
    if col < len(grid[0]) - 1:
        right = ((row, col + 1))  # Right
    if row < len(grid) - 1:
        down = ((row + 1, col))  # Down
    if col > 0:
        left = ((row, col - 1))  # Left
    if symbol == "|":
        if rc in get_neighbors_easy(up, grid):
            if rc in get_neighbors_easy(down, grid):
                neighbors = [up, down]
            else:
                neighbors = [up]
        elif rc in get_neighbors_easy(down, grid):
            neighbors = [down]

    elif symbol == "-":
        if rc in get_neighbors_easy(left, grid):
            if rc in get_neighbors_easy(right, grid):
                neighbors = [left, right]

            else:
                neighbors = [left]

        elif rc in get_neighbors_easy(right, grid):
            neighbors = [right]
    
    elif symbol == "L":
        if rc in get_neighbors_easy(up, grid):
            if rc in get_neighbors_easy(right, grid):
                neighbors = [up, right]

            else:
                neighbors = [up]

        elif rc in get_neighbors_easy(right, grid):
            neighbors = [right]

    elif symbol == "J":
        if rc in get_neighbors_easy(left, grid):
            if rc in get_neighbors_easy(up, grid):
                neighbors = [left, up]

            else:
                neighbors = [left]

        elif rc in get_neighbors_easy(up, grid):
            neighbors = [up]

    elif symbol == "7":
        if rc in get_neighbors_easy(left, grid):
            if rc in get_neighbors_easy(down, grid):
                neighbors = [left, down]

            else:
                neighbors = [left]

        elif rc in get_neighbors_easy(down, grid):
            neighbors = [down]
    elif symbol == "F":
        if rc in get_neighbors_easy(down, grid):
            if rc in get_neighbors_easy(right, grid):
                neighbors = [down, right]
            else:
                neighbors = [down]
        elif rc in get_neighbors_easy(right, grid):
            neighbors = [right]
    elif symbol == ".":
        neighbors = []
    elif symbol == "S":
        print(up, down, left, right)
        neighbors = [up, down, left, right]
    neighbors = [gs(grid, n) for n in neighbors]
    return neighbors



data = get_data(day=10, year=2023).splitlines()

data = open("day10/input.txt", "r").readlines()
#data = open("day10/test.txt", "r").readlines()


matrix = [["."]*(len(data[0])+1)]
rowc = 0
index_s = []
for d in data:
    d = d.strip()
    d = "."+d+"."
    matrix.append(list(d))
    try:
        colc = indexOf(d, "S")
        index_s = (rowc, colc)
    except Exception as e:
        pass
    rowc += 1

matrix.append(["."]*(len(data[0])+1))
s_neighbours = []
G = nx.DiGraph()
index_s = (50, 97)
seen = [('S', (50, 97)),('F', (50, 96))]
wc = 0
while True:
    wc += 1
    get_next = get_neighbors(seen[-1][1], matrix)
    if wc > 4 and ('S', (50, 97)) in get_next:
        break
    for n in get_next:
        if n not in seen:
            seen.append(n)


from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
path = [s[1] for s in seen]
polygon = Polygon(path)

tot = 0
for r in tqdm(range(len(matrix))):
    for c in range(len(matrix[0])):
        if (r,c) not in path:
            if polygon.contains(Point(r,c)):
                tot += 1

print('shapely tot',tot)


import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_grid(size, density):
    grid = [['T' if random.random() < density else ' ' for _ in range(size)] for _ in range(size)]
    return grid

def spread_fire(grid, ignition_prob):
    new_grid = [row.copy() for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'T':
                if i > 0 and random.random() < ignition_prob:
                    new_grid[i - 1][j] = 'T'
                if i < len(grid) - 1 and random.random() < ignition_prob:
                    new_grid[i + 1][j] = 'T'
                if j > 0 and random.random() < ignition_prob:
                    new_grid[i][j - 1] = 'T'
                if j < len(grid[i]) - 1 and random.random() < ignition_prob:
                    new_grid[i][j + 1] = 'T'
    return new_grid

def update(frame):
    global grid
    grid = spread_fire(grid, ignition_prob)
    im.set_array([[1 if cell == 'T' else 0 for cell in row] for row in grid])
    return im,

size = 10
density = 0.2
ignition_prob = 0.3
iterations = 20

grid = initialize_grid(size, density)

fig, ax = plt.subplots()
im = ax.imshow([[1 if cell == 'T' else 0 for cell in row] for row in grid], cmap='Reds', animated=True)

ani = animation.FuncAnimation(fig, update, frames=iterations, blit=True)

plt.show()
