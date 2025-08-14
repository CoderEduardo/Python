"""class Aluno:
    def __init__(self, nome, idade, nota):  ##construt
        self.nome = nome
        self.idade = idade
        self.nota = nota    

    ##Criando métodos para a classe Aluno
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}") 


aluno1 = Aluno("João", 20, 8.5)
aluno2 = Aluno("Maria", 22, 9.0)

#chamar método da classe Aluno
aluno1.mostrar_informacoes()
aluno2.mostrar_informacoes()"""

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self, nome,nota):
        super().__init__(nome)
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"


"""aluno1 = Aluno("João", 8.5)
aluno2 = Aluno("Maria", 5.0)    
aluno3 = Aluno("Ana", 7.0) 

print(aluno1.verificar_aprovacao())
print(aluno2.verificar_aprovacao())   
print(aluno3.verificar_aprovacao())"""

alunos = [
    Aluno("João", 8.5),
    Aluno("Maria", 5.0),
    Aluno("Ana", 7.0)
]

for aluno in alunos:
    print(f"{aluno.nome}: {aluno.verificar_aprovacao()}")
