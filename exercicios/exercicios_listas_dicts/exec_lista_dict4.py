"""
Filtrar valores de um dicionário
Dado um dicionário com nomes de produtos como chave e a quantidade em estoque como valor, crie uma nova
 lista apenas com os produtos que tenham mais de 10 unidades em estoque."""

lista_prod = []
produtos = {"Caneta": 5,
            "Lápis": 22,
            "Borracha": 17,
            "Caderno": 8,
            "Lapiseira": 11,
            "Cola": 3}

for produto, qtd in produtos.items():
    if qtd > 10:
        lista_prod.append(produto)

print(lista_prod)
        

