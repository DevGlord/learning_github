import json

LOCAL_ARQUIVO = 'aprimorando.json'

class Paises:
    def __init__(self,nome_pais,ano_ido):
        self.nome_pais = nome_pais
        self.ano_ido = ano_ido

n1 = input('País:')
n2 = int(input('Ano de Nascimento:'))

n3 = input('País:')
n4 = int(input('Ano de Nascimento:'))

p1 = Paises((n1),(n2)) 
p2 = Paises((n3),(n4))

conjuntos = (vars(p1),vars(p2))

def fazendo_dump():
    print('Fazendo DUMP')
    with open(LOCAL_ARQUIVO,'w',encoding='utf8') as arquivo:
        json.dump(conjuntos,arquivo,ensure_ascii=False,indent=2)

if __name__ == '__main__':
    print('Ele é o __main__')
    fazendo_dump()
