numeros = [2,6,8,34,86,25,43]
frutas = ["Maça","Abacaxi","Damasco","Morango","Uva","Banana","Uva"]

#sorted() ordena a lista
numeros.sort()
frutas.sort()
#Os números ficam em ordem crescente e as strings em ordem alfabética
print(numeros)
print(frutas)

#Para reverter a formatação do sort() usamos o reverse = True
numeros.sort(reverse=True)
print(numeros)

#Para imprimir a mesma lista ao contrário usamos o reverse()
frutas.reverse()
print(frutas)

#Verficando quantos items tem dentro de uma lista
ocorrenciasUva = frutas.count("Uva")
print(ocorrenciasUva)

#Retornado o índice especifico de um item
indiceDamasco = frutas.index("Damasco")
print(indiceDamasco)