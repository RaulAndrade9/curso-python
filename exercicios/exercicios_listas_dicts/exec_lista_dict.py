"""
Lista de compras com preços
Crie um dicionário com pelo menos 5 produtos e seus respectivos preços.
Em seguida, faça uma lista com alguns desses produtos e calcule o total da compra.
"""
valor = 0
prod_price = {"Arroz": 10.00,
              "Feijão": 4.50,
              "Carne": 17.00,
              "Café": 8.00, 
              "Macarrão": 3.00,
              "Açúcar": 2.00}

compras = ["Arroz", "Feijão", "Carne"]

for i in range(0, len(compras)):
    if compras[i] in prod_price.keys():
        valor += prod_price[compras[i]]


print(f"O valor gasto nas compras foi de: {valor}")