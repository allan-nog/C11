import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

maior_populacao = paises.loc[paises["Population"].idxmax()]
print("País com a maior população:")
print(maior_populacao[["Country", "Region"]])
