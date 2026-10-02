import pandas as pd
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", sep=";")

america_latina = paises[
    paises["Region"].str.contains("LATIN AMER")
]

plt.figure()
plt.scatter(
    america_latina["GDP ($ per capita)"],
    america_latina["Literacy (%)"],
    s=america_latina["Population"] / 100000
)

plt.title("América Latina")
plt.xlabel("Renda per capita ($)")
plt.ylabel("Alfabetização (%)")
plt.tight_layout()
plt.show()  