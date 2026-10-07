import pandas as pd

seriesAno1 = pd.Series({"Java": 16.25, "C": 16.04, "Python": 9.85})
seriesAno2 = pd.Series({"C": 16.21, "Python": 12.12, "Java": 11.68})

variacao = seriesAno2 - seriesAno1

crescimento = variacao[variacao > 0]

print("Linguagens que cresceram:")
print(crescimento.round(2))