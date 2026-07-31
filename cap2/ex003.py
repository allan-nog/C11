sexo = ""

while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo(M/F): ').upper()

    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido! Digite novamente!')

if sexo == 'M':
    print('Homem')
else:
    print('Mulher')