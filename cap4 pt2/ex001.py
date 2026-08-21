import numpy as np

dataset = np.loadtxt('space.csv', delimiter = ';', dtype = 'str')

cond = dataset[1:, 7] == 'Success'

porcentagem = cond.sum() / len(cond) * 100

print(f'{porcentagem}%')