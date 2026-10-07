import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", sep=";")

regioes = paises[paises["Region"].str.contains("LATIN AMER|WESTERN EUROPE")]

sns.boxplot(data=regioes, x="Region", y="GDP ($ per capita)")

plt.title("Renda per capita por região")
plt.xlabel("Região")
plt.ylabel("Renda per capita")
plt.tight_layout()
plt.show()