import numpy as np 
import time
data = [1]

start = time.time()
a = np.array([])
for _ in range(10000):
    a = np.append(a, data)
print("append:", time.time() - start)

start = time.time()
b = []
for _ in range(10000):
    b.append(data)
b = np.concatenate(b)
print("concatenate:", time.time() - start)
