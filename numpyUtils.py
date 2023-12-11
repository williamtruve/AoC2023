import numpy as np
import numbers

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = np.array(matrix)

print(np.where(matrix > 5, matrix, 0)) #Map operation on ALL values
print(np.argwhere(matrix == 1)) #List of indices where condition is true
print(np.fill_diagonal(matrix, 0)) #Performs on matrix
print(matrix)
#print(np.linalg) bunch of values :)
print(matrix[0,0]) #Convenient indices

print(np.pad(matrix, 1)) #Outer ring of 0s

print(matrix.astype(int)) #Conversinon on everything