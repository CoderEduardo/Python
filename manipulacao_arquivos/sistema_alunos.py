# Classe Aluno
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota} - {self.verificar_aprovacao()}"

# Função para ler alunos do arquivo
def carregar_alunos():
    lista = []
    try:
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, nota = linha.strip().split(", ")
                lista.append(Aluno(nome, float(nota)))
    except FileNotFoundError:
        print("Arquivo alunos.txt não encontrado. Será criado ao adicionar novos alunos.")
    return lista

# Função para salvar um aluno no arquivo
def salvar_aluno(aluno):
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{aluno.nome}, {aluno.nota}\n")

# Lista inicial de alunos
alunos = carregar_alunos()

# Loop do menu
while True:
    print("\n=== Sistema de Alunos ===")
    print("1. Listar alunos")
    print("2. Adicionar aluno")
    print("3. Editar nota de aluno ")
    print("4. Excluir aluno")
    print("5. Listar alunos aprovados/reprovados")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            print(aluno)
    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        novo_aluno = Aluno(nome, nota)
        alunos.append(novo_aluno)
        salvar_aluno(novo_aluno)
        print(f"Aluno {nome} adicionado com sucesso!")
    elif opcao == "3":
        nome = input("Digite o nome do aluno para editar a nota: ")
        for aluno in alunos:
            if aluno.nome == nome:
                nova_nota = float(input(f"Digite a nova nota para {nome}: "))
                aluno.nota = nova_nota
                # Atualiza o arquivo com a nova nota
                with open("alunos.txt", "w") as arquivo:
                    for a in alunos:
                        arquivo.write(f"{a.nome}, {a.nota}\n")
                print(f"Nota de {nome} atualizada com sucesso!")
                break
        else:
            print(f"Aluno {nome} não encontrado.") 
    elif opcao == "4":
        nome = input("Digite o nome do aluno para excluir: ")
        for aluno in alunos:
            if aluno.nome == nome:
                alunos.remove(aluno)
                # Atualiza o arquivo removendo o aluno
                with open("alunos.txt", "w") as arquivo:
                    for a in alunos:
                        arquivo.write(f"{a.nome}, {a.nota}\n")
                print(f"Aluno {nome} excluído com sucesso!")
                break
        else:
            print(f"Aluno {nome} não encontrado.")
            
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
