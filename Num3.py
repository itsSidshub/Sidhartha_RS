import numpy as np
matrix = np.zeros((5, 5))
np.fill_diagonal(matrix, np.arange(1, 6))
print(matrix)
