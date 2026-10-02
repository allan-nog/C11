import pandas as pd
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", sep=";")

europa = paises[
    paises["Region"].str.contains("WESTERN EUROPE")
]

plt.figure(figsize=(12, 6))

plt.plot(
    europa["Country"],
    europa["GDP ($ per capita)"],
    "o-r",
    label="Renda per capita"
)

plt.plot(
    europa["Country"],
    europa["Phones (per 1000)"],
    "s--b",
    label="Telefones por 1000 habitantes"
)

plt.title("Europa Ocidental")
plt.xlabel("País")
plt.ylabel("Valor")
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()