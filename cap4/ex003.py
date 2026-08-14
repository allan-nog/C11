import numpy as np

matriz = np.zeros((2, 2))

linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)

matriz[linha, coluna] = 1

for i in range(3):
    linha_jogada = int(input("Linha (0 ou 1): "))
    coluna_jogada = int(input("Coluna (0 ou 1): "))

    if matriz[linha_jogada, coluna_jogada] == 1:
        print("Game Over! :( Try Again!")
        break

    if i == 2:
        print("Congratulations! You beat the game! :)")