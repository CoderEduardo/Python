from functools import reduce
import operator
#usando funções com listas

numeros = [6,3,8,15,2,7,14]

#Retornando a quantidade de itens de um lista
tamanho = len(numeros)
print(tamanho)

#Retornando o maior elemento da lista
maior_elemento = max(numeros)
print(maior_elemento)

#Retornando o menor elemento da lista
menor_elemento = min(numeros)
print(menor_elemento)

#Retornando a soma de todos os elementos da lista
soma = sum(numeros)
print(soma)

#Retornando a multiplicação de todos os elementos de uma lista
multiplicacao = reduce(operator.mul, numeros)
print(multiplicacao)

#Retornando a divisão de todos os elementos de uma lista
divisao = reduce(lambda x ,y : x / y, numeros)
print(divisao)

#Calculando a média dos valores
media = (sum(numeros)) / ((len(numeros)))
print(f"A média dos valore é de {media:.2f}")