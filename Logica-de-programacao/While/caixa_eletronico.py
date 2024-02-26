saldo = 1000

while True:
    print("Caixa Eletrônico\n 1 - Verificar Saldo \n 2 - Depositar Dinheiro \n 3 - Sacar Dinheiro \n 4 - Sair")
    opcao = int(input("Escolha uma opção (1-4):"))
    
    if opcao == 1:
        print(f"Seu saldo é de R${saldo:.2f}")
        
    elif opcao == 2:
        valor = int(input("Quanto de valor você quer depositar:"))
        if valor > 0:
             saldo += valor
        
    elif opcao == 3:
        sacar = int(input("O quanto você deseja sacar?"))
        
        if sacar <= saldo and sacar > 0:
            saldo -= sacar
        else:
            print("Ocorreu um erro no saque ou o saldo é invalido")
            
    elif opcao == 4:
        print("Obrigado por usar no caixa eletrônico.")
        break