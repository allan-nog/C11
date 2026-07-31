nome = input('Nome completo: ')

print(f'\n\nNome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome.replace(" ", ""))}')

partes = nome.split()
ultimoNome = partes[len(partes)-1]
print(f'Novo nome: {nome.replace(ultimoNome, "do Inatel")}')