import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str')

cond = dataset[1:, 1] == 'SpaceX'

spacex = dataset[1:][cond]

custos = spacex[:, 6].astype(float)

print(spacex[custos.argmax(), 4])