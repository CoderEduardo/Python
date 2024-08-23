#Conversão de strings para listas

#Ao usar a função list em uma string, cada caractere da string será um elemento da lista resultante 
s = "Olá, tudo bem?"
listas_s = list(s)
print(listas_s)

#Ao usar o .split() em uma lista, por padrão, cada caracter separado por um espaço será um novo item da lista
frase = "Python é divertido"
palavras = frase.split()        #Eu posso passar o parâmetro de divisão entre parênteses, .split("t")
print(palavras)

data = "22/08/2024"
elementos_data = data.split("/")
print(elementos_data)

#Conversão de listas para Strings

lista_palavras = ['Python','é','incrível']
frase_juntada = ' '.join(lista_palavras)        #Usamos join para converter uma lista em string, passando um divisor dos caracteres
print(frase_juntada)

lista_data = ["22","08","2024"]
data_juntada = "/".join(lista_data)
print(data_juntada)

#Exercícios

palavra = "Python"
lista_python = list(palavra)
print(lista_python)

frase2 = "Aprendendo Python é divertido"
lista_frase2 = frase2.split()
print(lista_frase2)

lista_juntada2 = " ".join(lista_frase2)
print(lista_juntada2)

frutas2 = ['Maça','Banana','Cereja']
frutas_juntadas = ", ".join(frutas2)
print(frutas_juntadas)