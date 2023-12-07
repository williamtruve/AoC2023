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


