#Adicionar elementos

#append() adiciona elementos no final da lista
frutas = ["Maça","Banana"]
frutas.append("Abacaxi")
print(frutas[-1])

#insert() adiciona um item em um índice especifico da lista
frutas.insert(1,"Abacate") #O primeiro parâmetro é o lugar da lista e o segundo é o item
print(frutas)

#Removendo elementos 

#remove() remove o primeiro elemento da lista que tem o seu valor especificado
frutas.remove("Banana")
print(frutas)

#pop() remove os itens por índice, ou o item do último índice se ele não for especificado
frutas.pop(1)
print(frutas)

#Concatenar listas

#+ une duas listas
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
uniao = lista1 + lista2
print(uniao)

#extend() adiciona os itens de uma lista ao final de 
lista1.extend(lista2)
print(lista1)

#Repetindo uma lista
repeticao = ["a","b","c"] * 3
print(repeticao)

#Verificar se um item está na lista
print("Maça" in frutas)