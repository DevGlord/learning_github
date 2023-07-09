class Escola:
    def __init__(self,nome_aluno,idade_aluno):
        self.nome_aluno = nome_aluno
        self.idade_aluno = idade_aluno
        
    def apresentacao_alunos(self):
        print(f'O {self.nome_aluno} tem {self.idade_aluno}')

n1 = str(input('Nome do aluno:'))
n2 = int(input('Idade do aluno:'))
c1 = Escola(n1,n2)
c1.apresentacao_alunos()