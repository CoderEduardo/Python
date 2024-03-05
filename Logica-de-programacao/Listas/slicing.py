lista = [0,1,2,3,4,5,6,7,8,9]

#Como acessar subcojuntos de listas
subconjutos = lista[1:4]
print(subconjutos)

#Omissão dos elementos
primeiros_elementos = lista[:2]
elementos_depois_do_indice_dois = lista[2:]
print(primeiros_elementos)
print(elementos_depois_do_indice_dois)

#Exibindo elementos alternados, ele vai exibir os elementos de dois em dois
elementos_alternados = lista[::2]
print(elementos_alternados)

#Exercicio 
cores = ["Vermelho","Verde","Azul","Amarelo","Laranja","Roxo","Marrom","Cinza"]
print(cores[1:3])
print(cores[:2])
print(cores[4:])
print(cores[::2])
print(cores[::-1])