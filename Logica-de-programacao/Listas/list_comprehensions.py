#List comprehensions é uma forma mais rápida de criar uma lista seguindo um certo padrão

#Criando uma lista com todos os quadrados de um número de 0 à 9
quadrados = [i**2 for i in range(10)]
print(quadrados)

#Criando ums lista mostrando apenas os quadrados de números pares 
quadrados_pares = [i**2 for i in range(10) if i % 2 == 0]
print(quadrados_pares)

#Mostrando apenas as combinações em que os resultados dão 5
a = [1,2,3,4,5]
b = [1,2,3,4,5]
resultado_5 = [(x , y) for x in a for y in b if x+y == 5]

#Criando uma lista com números elevados ao cubo
cubos = [x**3 for x in range(10)]
print(cubos)

#Criando uma lista de todos os números de 1 à 20 que são diviíveis por 3
divisiveis_3 = [i for i in range(20) if i % 3 == 0]
print(divisiveis_3)

#Criando uma lista apenas com frutas que possuem mais de 5 caracteres
frutas = ["Maça","Banana","Manga","Uva","Abacaxi","Laranja"]
conjunto = [fruta for fruta in frutas if len(fruta) > 5] 
print(conjunto)

#Criando outra lista com apenas notas acima de 75
notas = [89,92,56,78,45,34,90,99,65,76,80,82]
acima_media = [nota for nota in notas if nota > 75]
print(acima_media)