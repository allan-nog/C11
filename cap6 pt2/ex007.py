import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", sep=";")

sns.regplot(
    data=paises,
    x="Literacy (%)",
    y="Infant mortality (per 1000 births)",
    line_kws={"color": "red"}
)

plt.title("Alfabetização e mortalidade infantil")
plt.xlabel("Alfabetização (%)")
plt.ylabel("Mortalidade infantil por 1000 nascimentos")
plt.tight_layout()
plt.show()