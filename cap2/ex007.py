palavra = input('Digite uma palavra: ')
aPresente = False
qtdVogal = 0

for letra in palavra:
    letra = letra.upper()

    print(f'{letra}')
    if letra == 'A':
        aPresente = True
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        qtdVogal += 1

if aPresente == True:
    print(f'A letra A está presente e temos {qtdVogal} vogais.')
else:
    print(f'A letra A NÃO está presente e temos {qtdVogal} vogais.')