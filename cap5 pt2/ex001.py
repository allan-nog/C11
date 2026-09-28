import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

oceania = paises[paises["Region"].str.contains("OCEANIA")]
print("Países da Oceania:")
print(oceania["Country"])
print("Quantidade:", len(oceania))
