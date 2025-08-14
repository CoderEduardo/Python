nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"Obrigado {nome}, você é maior de idade.")
else:
    print(f"Obrigado {nome}, você é menor de idade.")


##Operador ternário

maioridade = "maior" if idade >= 18 else "menor"
print(f"Você é {maioridade} de idade.")



