#%%
nome_arquivo = "historia.txt"

#open_file = open(nome_arquivo, encoding="utf-8")
#conteudo = open_file.read()
#print(conteudo)
#open_file.close()

#%%
with open(nome_arquivo,encoding="utf-8")as open_file:
    conteudo = open_file.read()
    print(conteudo)