while True:
    print("Calculadora Simples: \n 1 - Adição\n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair ")
    opcao = int(input("Escolha uma opção:"))
    
    #a forma mais otimizada seria usando uma função dentro de cada condição, passando o valor aritmetico por parametro, porém não aprendemos isso ainda
    
    if opcao == 5:
        print("Obgrigado por usar nossa calculdora")
        break
    
    numero1 = float(input("Digite o primeiro número:")) 
    numero2 = float(input("Digite o segundo número:")) 
    
    if opcao == 1:
        resultado = numero1 + numero2
    elif opcao == 2:
        resultado = numero1 - numero2
    elif opcao == 3:
        resultado = numero1 * numero2 
    elif opcao == 4:
        resultado = numero1 / numero2

        
    print(f"Resultado: {resultado:.2f}")