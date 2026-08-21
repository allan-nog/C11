pessoas = []

for i in range(3):
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    pessoa = {'nome': nome, 'peso': peso}
    pessoas.append(pessoa)

mais_pesada = pessoas[0]
mais_leve = pessoas[0]

for pessoa in pessoas:
    if pessoa['peso'] > mais_pesada['peso']:
        mais_pesada = pessoa

    if pessoa['peso'] < mais_leve['peso']:
        mais_leve = pessoa

print("Mais pesada:", mais_pesada['nome'])
print("Mais leve:", mais_leve['nome'])