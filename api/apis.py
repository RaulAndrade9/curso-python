#%%
ceps = ["09851665", "09851661", "09820000", "09851180"]
#%%
import requests
import json
#%%
from tqdm import tqdm
#%%
import pandas as pd

#%%

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep = i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

#%%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")
#%%
for item in dados:
    print(item)
#%%
with open("ceps.json", "w", encoding="utf-8")as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)