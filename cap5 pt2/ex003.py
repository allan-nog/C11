import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

print("Média de alfabetização por região:")
print(paises.groupby("Region")["Literacy (%)"].mean())