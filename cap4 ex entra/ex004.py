import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

cond = dataset[1:, 1] == 'NORTHERN AMERICA'

print(cond.sum())