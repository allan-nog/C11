import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

setosa = iris[iris["species"] == "setosa"]

correlacao = setosa[["sepal_length", "sepal_width", "petal_length", "petal_width"]].corr()

sns.heatmap(correlacao, annot=True, fmt=".2f")

plt.title("Correlação das variáveis da setosa")
plt.tight_layout()
plt.show()