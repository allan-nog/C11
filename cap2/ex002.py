num = int(input('Digite um número: '))
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))

for i in range(inicio, fim+1):
    print(f'{num} * {i} = {num*i}')