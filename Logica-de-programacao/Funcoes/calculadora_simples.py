print("Calculadora Simples")

def somar(n1,n2):
     print(n1 + n2)

def subtrair(n1,n2):
     print(n1 - n2)

def dividir(n1,n2):
     print(n1 / n2)

def multiplicar(n1,n2):
     print(n1 * n2)

while True:
    
    opcao = int(input(" 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 5 - Sair\n"))
    
    if opcao == 5:
        print("Obrigado por usar a calculadora")
        break
    
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número:"))
    
    if opcao == 1:
       somar(numero1,numero2)
    elif opcao == 2:
        subtrair(numero1,numero2)
    elif opcao == 3:
        dividir(numero1,numero2)
    elif opcao == 4:
        multiplicar(numero1,numero2)
    

    