import numpy as np

dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str')

empresas, quantidade = np.unique(dataset[1:, 1], return_counts = True)

for i in range(len(empresas)):
    print(empresas[i], quantidade[i])