import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])

linhas = matriz.shape[0]
colunas = matriz.shape[1]

total = linhas * colunas

if total % 2 == 0:
    print("Pode tornar um vetor com numero par de eleentos")
else:
    print("Pode tornar um vetor com numero ímpar de eleentos")