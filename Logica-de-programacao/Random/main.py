import random
#Gera um número aleatório entre 1 e 100
print(random.randrange(1,100))
#Gera um número aleatório inteiro entre 1 e 5 
print(random.randint(1,5))
#Gera um número flutuante entre 0 e 1
print(random.random())

#Pegando um item aleátorio de uma lista
frutas = ['Maça','Abacate','Abacaxi','Morango','Uva']
print(random.choice(frutas))

#Embaralhando uma lista de números
numeros = [1,2,3,4,5,6]
random.shuffle(numeros)
print(numeros)

#Gerando um ponto flutuante entre números especificos
print(random.uniform(5.5,9.8))