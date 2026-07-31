distancia = int(input('Distância da viagem(km): '))

if distancia <= 200:
    precoPassagem = distancia * 0.50
else:
    precoPassagem = distancia * 0.45

print(f'O preço da sua passagem é R${precoPassagem}')