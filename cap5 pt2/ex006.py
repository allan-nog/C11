import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

estatisticas = paises.groupby("Region")["Population"].describe()
print("Cinco primeiras linhas das estatísticas:")
print(estatisticas.head())
