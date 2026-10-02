import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("space.csv", sep=";")

sucessos = space[space["Status Mission"] == "Success"]
falhas = space[space["Status Mission"] == "Failure"]

mais_sucessos = sucessos["Company Name"].value_counts().head(5)
mais_falhas = falhas["Company Name"].value_counts().head(5)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(mais_sucessos.index, mais_sucessos.values, color="green")
plt.title("Empresas com mais sucessos")
plt.ylabel("Quantidade de missões")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.bar(mais_falhas.index, mais_falhas.values, color="red")
plt.title("Empresas com mais falhas")
plt.ylabel("Quantidade de missões")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()