import pandas as pd
import matplotlib.pyplot as plt

space = pd.read_csv("space.csv", sep=";")

eua = space[space["Location"].str.endswith("USA")]
china = space[space["Location"].str.endswith("China")]

empresas_eua = eua["Company Name"].drop_duplicates()
empresas_china = china["Company Name"].drop_duplicates()

plt.figure()
plt.bar(
    ["EUA", "China"],
    [len(empresas_eua), len(empresas_china)]
)

plt.title("Quantidade de empresas espaciais")
plt.xlabel("País")
plt.ylabel("Quantidade")
plt.show()