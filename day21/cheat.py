

from termios import IXANY
from networkx import neighbors
from regex import F
from utils.aocutils import get_neighbors
from tqdm import tqdm
import numpy.polynomial.polynomial as poly
# 33445 = 131 + 65
# Y   X   Y   X   Y
n = 202300
print(14590*(n**2) + (14694*n) + 3691)


x = [65, 196, 327]
y = [3691, 32975, 91439]

def lagrange(values):
    a = values[0] / 2 - values[1] + values[2] / 2
    b = -3 * (values[0] / 2) + 2 * values[1] - values[2] / 2
    c = values[0]
    return a,b,c
print(lagrange(y))
# 1, 10, 18, 26, 34

#202301 full gardens to the left and right and up and down

#Fel 1223684317384900