#Usando Lambda para multiplicar números
dobrar = lambda n: n * 2
print(dobrar(5))

#Usando lambda com filter para mostrar apenas números pares
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = list(filter(lambda x : x % 2 == 0, lista_numeros))
print(numeros_pares)

#Usando uma função lambda como se fosse um if else
status = lambda n: "Negativo" if n < 0 else ("Zero" if n == 0 else "Positivo")
print(status(-4))

#Ordenando uma lista usando o sorted e o lambda, o sorte em strings ordena pela ordem alfabética e por números na ordem crescente
lista = [("João",35),("Maria",25),("Pedro",40)]
pessoas_ordenadas = sorted(lista,key=lambda x:x[1])
print(pessoas_ordenadas)

#Usando o lambda com map para retornar a quantidade de caracteres de cada item
nomes = ['Luis Eduardo','Katarina','José','Augusto Melo']
quantidade_letras = list(map(lambda x: len(x),nomes))
print(quantidade_letras)