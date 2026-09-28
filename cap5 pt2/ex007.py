import pandas as pd

paises = pd.read_csv("paises.csv", sep=";")

def reduzir_mortalidade(valor):
    return valor * 0.85

coluna = "Infant mortality (per 1000 births)"
mortalidade_original = paises[coluna]
mortalidade_reduzida = paises[coluna].apply(reduzir_mortalidade)
mortalidade_reduzida.name = "Meta com redução de 15%"

comparacao = pd.concat([mortalidade_original, mortalidade_reduzida], axis=1)
print("Comparação da mortalidade infantil:")
print(comparacao.to_string(index=False))