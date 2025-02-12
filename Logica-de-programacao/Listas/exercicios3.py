numeros = []

for  i in range (1,6):
    numero = int(input(f"Digite o valor do {i}° número: "))
    numeros.append(numero)

numeros.sort()
print(f"Números em ordem crescente: {numeros}")