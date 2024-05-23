"""Retornando apenas os números pares com lambda.
A lógica é a seguinte, eu preciso informar para o python que eu estou trabalhando com uma lista, e depois usar o filter para fazer um filtro,
logo em seguida eu uso a função lambda passando o indice x, e fazendo a lógica que eu quero, logo em seguida eu passo a minha lista
"""
numeros = [ 1, 2, 4, 5, 6, 7, 8, 9]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

#Retornando apenas os nomes que começam com a letra A
nomes = ["Lucas",'José',"Amanda","Luis","Carlos","Alice","Erilda","Antônio","Carlos"]
letraA = list(filter(lambda x: x[0] == "A",nomes))
print(letraA)

#Retornando quantos nomes especificos tem
quantidadeCarlos = len(list(filter(lambda x: x == "Carlos",nomes)))
print(quantidadeCarlos)

#Elevando todos números ao quadrado com a função map
numeros2 = [1,2,3,4,5,6]
numeros_ao_quadrado = list(map(lambda x: x**2,numeros2))
print(numeros_ao_quadrado)
#A função map aplica aos mesmo itens da lista uma operação desejada

#Retornando o comprimento de cada palavra
comprimentoPalavra = list(map(lambda x: len(x),nomes))
print(comprimentoPalavra)