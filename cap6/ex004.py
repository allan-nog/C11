import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("space.csv", sep=";")

falhas = space[space["Status Mission"] == "Failure"]

empresas = falhas["Company Name"].value_counts().head(5)

plt.figure()
plt.bar(empresas.index, empresas.values)

plt.title("Empresas com mais falhas")
plt.xlabel("Empresa")
plt.ylabel("Quantidade de falhas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()