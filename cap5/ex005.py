import pandas as pd

seriesAno1 = pd.Series({"Java": 16.25, "C": 16.04, "Python": 9.85})
seriesAno2 = pd.Series({"C": 16.21, "Python": 12.12, "Java": 11.68})

variacao = seriesAno2 - seriesAno1

seriesAno3 = seriesAno2 + variacao
seriesAno4 = seriesAno3 + variacao

print("Linguagem mais popular após mais dois anos:")
print(seriesAno4.nlargest(1).round(2))