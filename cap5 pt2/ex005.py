import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

def ajuda_humanitaria(taxa):
    if taxa < 9:
        return "Balanced"
    else:
        return "Urgent"

paises["Humanitarian Help"] = paises["Deathrate"].apply(ajuda_humanitaria)
print(paises.to_string(index=False))
