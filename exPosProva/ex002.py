import numpy as np

array1 = np.array(['Ana', 'Carlos', 'Bruna', 'Pedro'])
array2 = np.array(['Lucas', 'Mariana', 'João', 'Julia'])

array3 = np.concatenate((array1, array2))

array3 = array3.reshape(2, 4)

array3 = np.sort(array3)[::-1]

print(array3)