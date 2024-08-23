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

##funções
def adicionarItem(args):
    lista_compras.append(args)
    print(f"O item {args} foi adicionado!!!")

def removerItem(args):
        existe = None
        for elemento in lista_compras:
                existe = True if elemento == args else False      
        if existe:
            lista_compras.remove(args)
            print(f"O item {args} foi removido com sucesso")
        else:
            print(f"Não conseguimos apagar o item {args}, pois ele não estava cadastrador anteriormente")

def mostrarItens(args):
     if len(args) == 0:
            print("A sua lista ainda está vazia!!!")
     else:
        print("Lista de compras")
        for itens in args:
            print(f" - {itens}")

while entrada:

    opcao = str(input("\n 1. Adicinar item à lista \n 2. Remover item da lista \n 3. Exibir lista de compras \n 4. Sair \n"))

    ##Opcção que adiciona um noovo item
    if opcao == "1":
        item = str(input("Digite o nome do novo item: ")).lower()
        adicionarItem(item)
    
    ##Opção que remove um item
    elif opcao == "2":
        item = str(input("Digite o nome do item que você gostaria de remover: ")).lower()
        removerItem(item)

    ##Opção que exibe lista de compras
    elif opcao == "3":
        mostrarItens(lista_compras)
    
    #Opção de saída
    elif opcao == "4":
        break

    else:
        print("Digite uma opção válida!!!")


            

          

    

