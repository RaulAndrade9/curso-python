"""
Contagem de elementos em uma lista
Crie uma lista com alguns nomes de frutas.
 Em seguida, crie um dicionário que mostre quantas vezes cada fruta aparece na lista.
"""
frutas = ["banana", "laranja", "morango", "abacate", "abacate", "abacate", "laranja", "morango"]

dic_frutas = {}

for fruta in frutas:
    if fruta not in dic_frutas.keys():
        dic_frutas[fruta] = 1
    else:
        dic_frutas[fruta] += 1

print(dic_frutas)