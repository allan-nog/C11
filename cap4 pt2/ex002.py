import numpy as np

dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str')

custos = dataset[1:, 6].astype(float)

custos = custos[custos > 0]

print(custos.mean())