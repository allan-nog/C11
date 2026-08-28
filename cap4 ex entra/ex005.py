import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str')

cond = dataset[1:, 1] == 'LATIN AMER. & CARIB'

paises = dataset[1:][cond]

renda = paises[:, 8].astype(float)

print(paises[renda.argmax(), 0])