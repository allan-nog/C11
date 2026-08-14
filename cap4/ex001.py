import numpy as np

array1 = np.ones(8)
array2 = np.random.randint(0, 10, 8)
array3 = array1 + array2

if array3.sum() >= 40:
    array3 = array3.reshape(4, 2)
else:
    array3 = array3.reshape(2, 4)

print("Matriz: ")
print(array3)