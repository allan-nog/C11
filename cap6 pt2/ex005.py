import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", sep=";")

correlacao = paises[
    [
        "GDP ($ per capita)",
        "Literacy (%)",
        "Infant mortality (per 1000 births)",
        "Phones (per 1000)"
    ]
].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(correlacao, annot=True, fmt=".2f")

plt.title("Correlação dos dados dos países")
plt.tight_layout()
plt.show()