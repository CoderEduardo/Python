numero = int(input("Digite um número inteiro:"))
resultado = 0
for i in range(0,numero,+2):
    resultado += i

if numero % 2 == 0:
        resultado += numero
        
print(f"A soma dos números pares de 1 até {numero} é: {resultado}")