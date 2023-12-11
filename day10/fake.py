import random
import matplotlib.pyplot as plt

def initialize_grid(size, density):
    grid = [['#' if random.random() < density else ' ' for _ in range(size)] for _ in range(size)]
    return grid

def spread_fire(grid, ignition_prob, start_points):
    new_grid = [row.copy() for row in grid]
    for start_point in start_points:
        i, j = start_point
        if grid[i][j] == '#':
            if i > 0 and grid[i - 1][j] != '#':
                new_grid[i - 1][j] = '#'
            if i < len(grid) - 1 and grid[i + 1][j] != '#':
                new_grid[i + 1][j] = '#'
            if j > 0 and grid[i][j - 1] != '#':
                new_grid[i][j - 1] = '#'
            if j < len(grid[i]) - 1 and grid[i][j + 1] != '#':
                new_grid[i][j + 1] = '#'
    return new_grid

def plot_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

size = 10
density = 0.2
ignition_prob = 1.0  # Set to 1.0 to ensure immediate ignition from starting points
iterations = 20

# Choose starting points (replace with your desired points)
start_points = [(2, 2), (7, 7)]

grid = initialize_grid(size, density)

for _ in range(iterations):
    grid = spread_fire(grid, ignition_prob, start_points)
    plot_grid(grid)
    input("Press Enter to continue...")  # Press Enter to see the next frame

