import numpy as np

array1 = np.arange(0, 51, 2)
array2 = np.arange(100, 50, -2)

array3 = np.concatenate((array1, array2))
array3 = np.sort(array3)

print(array3)