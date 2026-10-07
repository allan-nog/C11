import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

space = pd.read_csv("space.csv", sep=";")

space.columns = space.columns.str.strip()

com_custo = space[space["Cost"] > 0]

sns.boxplot(data=com_custo, x="Status Rocket", y="Cost")

plt.title("Custo das missões por status do foguete")
plt.xlabel("Status do foguete")
plt.ylabel("Custo")
plt.show()