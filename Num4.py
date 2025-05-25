import numpy as np 
arr = np.random.rand(5, 5)
border = np.concatenate((arr[0], arr[-1], arr[1:-1, 0], arr[1:-1, -1]))
print(border)
