numero = 0
print("Todos os número que você digitar será somado, e só vamos parar quando você digitar 0")

while True:
    numeroDigitado = int(input("Digite um número:"))
    numero += numeroDigitado
    if numeroDigitado == 0:
        print(f"Soma de todos os números {numero}")    
        break    