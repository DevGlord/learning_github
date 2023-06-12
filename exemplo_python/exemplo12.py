import json

LOCAL_ARQUIVO = 'aprimorando.json'

class Paises:
    def __init__(self,nome_pais,ano_ido):
        self.nome_pais = nome_pais
        self.ano_ido = ano_ido

p1 = Paises('Portugal',2017) 
p2 = Paises('Afríca do Sul',2020)

conjuntos = (vars(p1),vars(p2))

with open(LOCAL_ARQUIVO,'w',encoding='utf8') as arquivo:
    json.dump(conjuntos,arquivo,ensure_ascii=False,indent=2)

