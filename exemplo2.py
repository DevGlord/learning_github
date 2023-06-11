import json

ARQUIVO = 'exemplo2.json'

class Carro:
    def __init__(self,nome,ano_comprado):
        self.nome = nome
        self.ano_comprado = ano_comprado
        

Car1 = Carro('Ferrari', 2022)
Car2 = Carro('Ford', 2012)
juntando_arquivos = (vars(Car1), vars(Car2))

with open(ARQUIVO,'w',encoding='utf8') as arquivo:
    json.dump(juntando_arquivos,arquivo,ensure_ascii=False,indent=2)
