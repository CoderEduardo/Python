for i in range (1,11):
    print(f"{i} - ", "par" if i % 2 == 0 else "ímpar")

"""for i in range(1,7):
    notas = float(input(f"Digite a nota {i}: "))
    print("Aprovado" if notas >= 6 else "Reprovado")


numero = int(input("Digite um número: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

contador = 1    
while contador <= 10:
    print(f"{contador} - ", "par" if contador % 2 == 0 else "ímpar")
    contador += 1

nota = 1
while nota > 0:
    nota = float(input("Digite a sua nota: (para sair digite uma nota negativa) "))
    if nota >= 0:  # só imprime se a nota for válida
        print("Aprovado" if nota >= 6 else "Reprovado")"""

i = 1
numero = int(input("Digite um número: "))
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

    