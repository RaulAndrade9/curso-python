"""
Conversão de lista para dicionário
Dada uma lista com os nomes de alguns países, crie um dicionário onde cada país seja
 a chave e o valor seja a quantidade de letras do nome do país."""

paises = ["Brasil", "Argentina", "Portugal", "Inglaterra", "Chile", "Japão"]
dicionario_paises = {}

for pais in paises:
    chave = pais
    valor = len(pais)
    dicionario_paises[chave] = valor

print(dicionario_paises)