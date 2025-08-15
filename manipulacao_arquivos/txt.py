##escrever em um arquivo de texto 
"""with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo\n")

##ler um arquivo de texto
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

##adicionar conteúdo a um arquivo de texto sem apagar o conteúdo existente
with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Adicionando uma nova linha\n")"""

with open("alunos.txt", "w") as arquivo:
    arquivo.write("Ana, 8.5\nBruno, 5.0\nCarlos, 7.0\n")

def verifica_aprovacao(nota):
    return "Aprovado" if nota >= 6.0 else "Reprovado"

with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(", ")
        nota = float(nota)
        status = verifica_aprovacao(nota)
        print(f"{nome} - {status}")