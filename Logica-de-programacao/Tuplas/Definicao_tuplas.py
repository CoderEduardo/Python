#Criando uma tupla 
livro = ("A arte da guerra","Sun Tzu","1544124123")
nome = livro[0]
autor = livro[1]
isbn = livro[2]

print(nome)
print(autor)
print(isbn)

#Também conseguimos cria tuplas sem usar os parênteses
teste = "Olá", "Salve", "Dale é os guri"

#Conseguimos transformar uma lista em uma tupla
lista = ['Bom dia','Sábado','Domingo']
tupla = tuple(lista)

produto = ("Laptop", 10, 1.500)
nome = produto[0]
quantidade = produto[1]
informacoes = produto[:-1]
print(informacoes)