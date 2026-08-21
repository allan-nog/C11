import numpy as np

dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str')

cond = np.char.find(dataset[1:, 2], 'USA') >= 0

print(cond.sum())