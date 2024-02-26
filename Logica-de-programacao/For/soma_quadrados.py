numero = int(input("Digite o número desejado de quadrados:"))
soma = 0

for i in range (1, numero+1):
    quadrado = i**2
    soma += quadrado
    print(f"Quadrado de {i} é: {quadrado}")
    
print(f"A soma de todos os quadrados é de {soma}")