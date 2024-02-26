import random 
numeroSorteado = random.randint(1,100)
tentativas = 0
print("Acerte o número entre 1 e 100")

while True:
    numero = int(input("Digite um número:"))
    tentativas += 1
    
    if numero < numeroSorteado:
        print("O número sorteado é maior")
    elif numero > numeroSorteado:
        print("O número sorteado é menor")
    else:
        print(f"Parabéns, você acertou o número sorteado {numeroSorteado}, em {tentativas} tentativas")
        

    
