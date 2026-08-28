import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

print(dataset[1:, [0, 1, 2, 3]])