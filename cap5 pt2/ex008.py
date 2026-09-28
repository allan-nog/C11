import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

paises_sem_coastline = paises.drop(columns=["Coastline (coast/area ratio)"])
paises_sem_coastline.to_csv("paises_sem_coastline.csv", sep=";", index=False)