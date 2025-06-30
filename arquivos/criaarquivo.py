arquivo = "registro.txt"

with open(arquivo, 'a', encoding="utf-8") as registro:
    registro.write(input("Digite algo "))
    registro.write("\n")
