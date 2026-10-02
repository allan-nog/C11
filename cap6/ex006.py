import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("space.csv", sep=";")

ativos = space[space["Status Rocket"] == "StatusActive"]
aposentados = space[space["Status Rocket"] == "StatusRetired"]

plt.figure()
plt.pie(
    [len(ativos), len(aposentados)],
    labels=["Ativos", "Aposentados"],
    autopct="%1.1f%%"
)

plt.title("Status dos foguetes")
plt.show()