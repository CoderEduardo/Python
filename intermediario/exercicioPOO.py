class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self, nome, nota):
        super().__init__(nome)
        self.nota = nota

    def verificar_aprovacao(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"
                       
    def __str__(self):
        return f"{self.nome} - Nota: {self.nota} - {self.verificar_aprovacao()}"  

alunos = [

    Aluno("Ana", 8.5),  
    Aluno("Bruno", 5.0),    
    Aluno("Carla", 7.0)

]                 

for aluno in alunos:
    print(aluno)