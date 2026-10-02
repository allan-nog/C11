import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("space.csv", sep=";")

roscosmos = space[space["Company Name"] == "Roscosmos"]

sucessos = roscosmos[roscosmos["Status Mission"] == "Success"]
falhas = roscosmos[roscosmos["Status Mission"] != "Success"]

plt.figure()
plt.pie(
    [len(sucessos), len(falhas)],
    labels=["Deram certo", "Deram errado"],
    autopct="%1.1f%%"
)

plt.title("Missões da Roscosmos")
plt.show()