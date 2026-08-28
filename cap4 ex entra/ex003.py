import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

alfabetizacao = dataset[1:, 9].astype(float)

print(alfabetizacao.mean())