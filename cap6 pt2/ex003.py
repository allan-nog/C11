import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.boxplot(data=titanic, x="class", y="age", hue="sex")

plt.title("Idades por classe e sexo")
plt.xlabel("Classe")
plt.ylabel("Idade")
plt.show()