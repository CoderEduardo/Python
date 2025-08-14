"""def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Luis Eduardo")
saudacao("Maria")
saudacao("João")

def imprimir_aluno(nome,idade, nota):
    print(f"O aluno {nome} tem {idade} anos e sua nota é {nota}")

imprimir_aluno("Luis Eduardo", 20, 9.5)   

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

m = media(7, 8, 9)
print(f"A média é: {m}")

def verifica_aprovacao(nota):
    if nota>=6:
        return "Aprovado"
    else:
        return "Reprovado"

print(verifica_aprovacao(7.5))
print(verifica_aprovacao(5.0))"""

alunos = [
    {"nome": "Alice", "nota": 8},
    {"nome": "Bob", "nota": 5},
    {"nome": "Carlos", "nota": 7}
]

def verifica_aprovacao(alunos):
    for aluno in alunos: 
        print(f"{aluno['nome']}: ", "aprovado" if aluno['nota'] >= 6 else "reprovado")

verifica_aprovacao(alunos)        
