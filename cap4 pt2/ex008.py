import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str')

custos = dataset[1:, 6].astype(float)

posicao = custos.argmax()

print(dataset[posicao + 1, 1])
print(custos[posicao])