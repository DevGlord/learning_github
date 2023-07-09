import json

LOCAL_ARQUIVO = 'ex1.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

person = Pessoa('Max',19)

person = Pessoa('Maateus',19)

people = Pessoa('Mario',21)

conjunto = (vars(person),vars(people))

with open(LOCAL_ARQUIVO,'w',encoding='utf8') as arquivo:
    json.dump(conjunto,arquivo,ensure_ascii=False,indent=2)


    
