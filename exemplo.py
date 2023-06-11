import json

LOCAL_ARQUIVO = 'ex1.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
<<<<<<< HEAD

person = Pessoa('Max',19)
=======
person = Pessoa('Mateus',19)
>>>>>>> page_contato
people = Pessoa('Mario',21)

conjunto = (vars(person),vars(people))

with open(LOCAL_ARQUIVO,'w',encoding='utf8') as arquivo:
    json.dump(conjunto,arquivo,ensure_ascii=False,indent=2)

with open(LOCAL_ARQUIVO,'r') as arquivo:
    print(json.load(arquivo))
    
