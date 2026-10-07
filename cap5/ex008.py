import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, [5, 4])
)

recorte = df.loc[["A", "C", "E"], ["X", "Y"]]

print("Recorte:")
print(recorte)

print("Soma de cada linha:")
print(recorte.sum(axis=1))

print("Soma de cada coluna:")
print(recorte.sum(axis=0))