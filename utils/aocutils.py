def get_neighbors(row, col, grid):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if col < len(grid[0]) - 1:
        neighbors.append((row, col + 1))  # Right
    if row < len(grid) - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    return neighbors


def get_neighbors_with_diagonal(row, col, grid):
    neighbors = get_neighbors(row, col, grid)
    rows, cols = len(grid), len(grid[0])

    if row > 0 and col > 0:
        neighbors.append((row - 1, col - 1))  # Up-Left
    if row > 0 and col < cols - 1:
        neighbors.append((row - 1, col + 1))  # Up-Right
    if row < rows - 1 and col > 0:
        neighbors.append((row + 1, col - 1))  # Down-Left
    if row < rows - 1 and col < cols - 1:
        neighbors.append((row + 1, col + 1))  # Down-Right

    return neighbors


def get_neighbors_wrap_around(row, col, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])

    neighbors.append(((row - 1 + rows) % rows, col))  # Up with wrap around
    neighbors.append((row, (col + 1) % cols))  # Right with wrap around
    neighbors.append(((row + 1) % rows, col))  # Down with wrap around
    neighbors.append((row, (col - 1 + cols) % cols))  # Left with wrap around

    return neighbors


def get_neighbors_with_diagonal_wrap_around(row, col, grid):
    neighbors = get_neighbors_wrap_around(row, col, grid)
    rows, cols = len(grid), len(grid[0])

    neighbors.extend([
        ((row - 1 + rows) % rows, (col - 1 + cols) % cols),  # Up-Left with wrap around
        ((row - 1 + rows) % rows, (col + 1) % cols),  # Up-Right with wrap around
        ((row + 1) % rows, (col - 1 + cols) % cols),  # Down-Left with wrap around
        ((row + 1) % rows, (col + 1) % cols),  # Down-Right with wrap around
    ])
    return neighbors
def rotate_matrix_90_clockwise(matrix):
    # Transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]

    # Reverse each row to get the final rotated matrix
    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]

    return rotated_matrix
import networkx as nx

# Create a graph
G = nx.DiGraph()

G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=3)

# Find the shortest path from 'A' to 'D'
shortest_path = nx.shortest_path(G, source='A', target='D', weight='weight')

shortest_path = nx.shortest_path_length(G, source='A', target='D', weight='weight')


import numpy as np

class Matrix(object):
    def __init__(self,x=None,y=None):
        if y == None:
            self.rows = 0
            for l in open(x).readlines():
                self.cols = len(l.strip())
                self.rows += 1

            self.a = np.ndarray((self.rows,self.cols),dtype='S1')

            r = 0
            for l in open(x).readlines():
                for c in range(self.cols):
                    self.a[r,c] = l[c]
                r += 1
        else:
            self.rows = x[0]
            self.cols = x[1]

            self.a = np.ndarray((self.rows,self.cols),dtype='S1')
            
            for r in range(self.rows):
                for c in range(self.cols):
                    self.a[r,c] = y
                    
    def set(self,r,c,v):
        self.a[r,c] = v

    def fill(self,v):
        for r in range(self.rows):
            for c in range(self.cols):
                self.a[r,c] = v

    def get(self,r,c):
        return self.a[r,c]

    def dims(self):
        return (self.rows,self.cols)

    def valid(self,rc):
        r = rc[0]
        c = rc[1]
        return r >= 0 and c >= 0 and r < self.rows and c < self.cols

    # get all neighbours
    def neighbours(self,rc,diagonals=False):
        r = rc[0]
        c = rc[1]
        if diagonals:
            n = [(r-1,c),(r+1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r-1,c+1),(r+1,c-1)]  # with diagonals
        else:
            n = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]  # no diagonals
        return [*filter(lambda x : self.valid(x),n)]

    def show(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(str(self.a[r,c])[2],end="")
            print()
        
    def count(self,ch):
        tot = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.a[r,c] == ch:
                    tot += 1
        return tot

