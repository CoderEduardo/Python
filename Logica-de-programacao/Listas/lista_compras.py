"""
    Exercício: Lista de compras

    Crie um programa em Python que permita ao usuário adicionar itens a uma lista de compras. O programa deve exibir um menu com as seguintes opções:

    1. Adicionar item à lista
    2. Remover item da lista
    3. Exibir lista de compras
    4. Sair

"""

lista_compras = []
entrada = True

while entrada:

    opcao = int(input("\n 1. Adicinar item à lista \n 2. Remover item da lista \n 3. Exibir lista de compras \n 4. Sair \n"))

    ##Opcção que adiciona um noovo item
    if opcao == 1:
        item = str(input("Digite o nome do novo item: ")).lower()
        lista_compras.append(item)
        print(f"O item {item} foi adicionado!!!")
    
    ##Opção que remove um item
    elif opcao == 2:
        item = str(input("Digite o nome do item que você gostaria de remover: ")).lower()

        for elemento in lista_compras:
             existe = True if elemento == item else False

        if existe:
            lista_compras.remove(item)
            print(f"O item {item} foi removido com sucesso")
        else:
            print(f"Não conseguimos apagar o item {item}, pois ele não estava cadastrador anteriormente")
        
    ##Opção que exibe lista de compras
    elif opcao == 3:
        if len(lista_compras) == 0:
            print("A sua lista ainda está vazia!!!")
        else:
            for itens in lista_compras:
                print("Lista de compras")
                print(f" - {itens}")
    
    #Opção de saída
    elif opcao == 4:
        break

    else:
        print("Digite uma opção válida!!!")
            

          

    

