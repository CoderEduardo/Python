maiorNumero = -1
print("Digite qualquer número inteiro, depois mostrarei o maior número digitado por você.\nDigitar um número menor que 0 é a condição de saida")
numeroDigitado = int(input("Digite um número:"))

while numeroDigitado > 0:
    numeroDigitado = int(input("Digite um número:"))
    if numeroDigitado > maiorNumero:
        maiorNumero = numeroDigitado
print(f"O maior número digitado foi {maiorNumero}")