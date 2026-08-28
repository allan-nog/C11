import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

regioes, quantidade = np.unique(dataset[1:, 1], return_counts=True)

print(regioes)
print(quantidade)