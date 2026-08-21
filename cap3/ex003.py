nome = input("Nome: ")
media = float(input("Média: "))

aluno = {'nome': nome, 'media': media}

if media >= 50:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

print(aluno)