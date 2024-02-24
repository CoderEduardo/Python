numero_secreto = 7 
numero = int(input("Adivinhe um número secreto entre 1 e 10 \n"))

if numero_secreto == numero:
    print("Parabens, você acertou o número secreto")
else:
    print("Você errou o número secreto")