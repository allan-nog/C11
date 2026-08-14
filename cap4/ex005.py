import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))

print("Média das linhas: ")
print(matriz.mean(axis=1))

print("Média das colunas: ")
print(matriz.mean(axis=0))

print("Maior média das linhas: ")
print(matriz.mean(axis=1).max())

print("Maior média das colunas: ")
print(matriz.mean(axis=0).max())

numeros, quantidade = np.unique(matriz, return_counts=True)

print("Quantidade de aparições:")
print(numeros)
print(quantidade)

print("Números que aparecem 2 vezes:")
print(numeros[quantidade == 2])