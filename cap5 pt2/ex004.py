import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

noCoast = paises[paises["Coastline (coast/area ratio)"] == 0]
print("Países sem costa marítima:")
print(noCoast["Country"])
noCoast.to_csv("noCoast.csv", sep=";", index=False)