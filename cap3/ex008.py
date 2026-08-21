produtos = []

for i in range(3):
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    produtos.append(produto)

for produto in produtos:
    total = produto['preco'] * produto['quantidade']
    print(produto['nome'], total)