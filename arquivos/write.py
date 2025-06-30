nome_arquivo = "historia_02.txt"
txt = "Novo arquivo"
with open(nome_arquivo, 'w', encoding="utf-8")as open_file:
    open_file.write(txt)