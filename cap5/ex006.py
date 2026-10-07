import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, [5, 4])
)

colunaX = df["X"]
menores = colunaX[colunaX < 30]

print("Média dos valores de X menores que 30:")
print(menores.mean())