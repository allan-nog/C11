import pandas as pd
import matplotlib.pyplot as plt

paises = pd.read_csv("paises.csv", sep=";")

america_norte = paises[
    paises["Region"].str.contains("NORTHERN AMERICA")
]

plt.figure()

plt.plot(
    america_norte["Country"],
    america_norte["Deathrate"],
    label="Mortalidade"
)

plt.plot(
    america_norte["Country"],
    america_norte["Birthrate"],
    label="Natalidade"
)

plt.title("América do Norte")
plt.xlabel("País")
plt.ylabel("Taxa")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()