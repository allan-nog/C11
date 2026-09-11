musicas = []

while True:
    nome = input("Nome da música: ")
    ano = int(input("Ano: "))

    musica = {
        'nome': nome,
        'ano': ano
    }

    musicas.append(musica)

    continuar = input("Deseja cadastrar outra música? (s/n): ")

    if continuar == 'n':
        break

print("Quantidade de músicas:", len(musicas))

ano_antigo = musicas[0]['ano']

for musica in musicas:
    if musica['ano'] < ano_antigo:
        ano_antigo = musica['ano']

print("Música(s) mais antiga(s):")

for musica in musicas:
    if musica['ano'] == ano_antigo:
        print(musica)