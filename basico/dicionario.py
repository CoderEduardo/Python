pessoa = {"nome":"Luis", "idade": 30, "cidade":"São Paulo"}
print(pessoa["nome"])
pessoa["idade"] = 20 #alterando valor
pessoa["profissao"] = "Engenheiro" #adicionando nova chave

aluno = {}
aluno["nome"] = str(input("Digite o seu nome: "))
aluno["idade"] = int(input("Digite a sua idade: "))
aluno["nota"] = float(input("Digite a sua nota: "))
print(f"o aluno {aluno['nome']} tem {aluno['idade']} anos e nota {aluno['nota']}")