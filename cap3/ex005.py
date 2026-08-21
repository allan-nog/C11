n = int(input("Quantidade de pessoas: "))

soma_idades = 0
mulheres_menos_20 = 0

for i in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")

    soma_idades += idade

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media = soma_idades / n

print("Média de idade:", media)
print("Mulheres com menos de 20 anos:", mulheres_menos_20)