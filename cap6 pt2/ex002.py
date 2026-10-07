import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.histplot(data=titanic, x="age", hue="sex", kde=True)

plt.title("Distribuição das idades por sexo")
plt.xlabel("Idade")
plt.ylabel("Quantidade de passageiros")
plt.show()