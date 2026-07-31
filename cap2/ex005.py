num = int(input('Digite um número entre 1000 e 9999: '))

if num < 1000 or num > 9999:
    print('Número inválido!')
else:
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10
    milhar = num // 1000

    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")