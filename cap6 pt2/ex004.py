import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")

sns.regplot(data=mpg, x="horsepower", y="mpg")

plt.title("Potência e rendimento do combustível")
plt.xlabel("Potência")
plt.ylabel("Milhas por galão")
plt.show()