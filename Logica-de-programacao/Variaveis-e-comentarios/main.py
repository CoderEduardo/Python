#Para fazer um comentário em python basta usar o o hashtag

"""
Outra forma de fazer comentários é usando as aspas, dessa forma conseguimos usar varias linhas
"""

#O que define o tipo da variavel e a forma que você declara ela

#Variável String
string = "Luis Eduardo"
#Variável Int
inteiro = 42 
#Variável Float
racional = 5.5
#Variável Complex, usado para calculos especificos
complexo = 5 + 5j

#Variável list
lista = [1,2,3]
#Variável tuple
tupla = (6,7,8)
#A diferença entre list e tuple é que a list pode ser alterada depois de criada e a tuple não, ambas são ordenadas

#Variável conjunto
conjunto = {3,2,5}  #Lista não ordenada que não se repete
#Variável dict
dicionario = {"chave":"valor"} #Uma coleção não ordenada de pares chave-valor
#Variável Booleano
booleano = True #São variáveis verdadeiras ou falsas
#Variável None
nenhum = None #Representa a ausência de valor

print(string,inteiro,racional,complexo,lista,tupla,conjunto,dicionario,booleano,nenhum)

#Para saber um tipo de variável basta usar o type()
print(type(complexo))

#Declarando varias variáveis ao mesmo tempo
var1, var2, var3, var4 = "Texto1", "Texto2","Texto3","Texto4"
print(var4)

#Para atribuir o mesmo valor a varias variáveis diferentes fazemos o seguinte
var5 = var6 = var7 = var8 = "Ana Paula"
print(var5,var6,var7,var8) 

#Se tiver uma coleção de valores em uma lista podemos extrair em variáveis, isso é chamado descompactar 
exemplo = "Texto1", "Texto2","Texto3","Texto4"
var9, var10, var11, var12 = exemplo 
print(var9,var10,var11,var12)