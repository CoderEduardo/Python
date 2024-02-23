#Conseguimos imprimir a letra especifica
posicaoLetra = "Python"
print(posicaoLetra[1])

#Recortando uma frase
frase = "Olá, mundo"
parte = frase[4:8]
print(parte)

#Verificando se existe uma palavra dentro da frase
frase2 = "O python é muito legal"
print("python" in frase2)
print("abacate" in frase2)

#Outra forma de verificar
if "python" in frase2:
    print("Sim, essa palavra está na frase")
else:
    print("Essa palavra não está na frase")

#Remover espaços em brancos de uma string do inicio ao final
frase3 = "                 Quantos dias tem um ano e 2 meses?                "
print(frase3.strip())

#Dividindo uma frase em uma lista
frase4 = "Olá, como vai você?"
print(frase4.split())

#Juntando uma lista em uma frase
palavras = ["Hoje","é","um","dia","especial"]
frase5 = ' '.join(palavras)         #Antes do .join temos uma aspas com espaço, que é o separador comum de cada elemento
print(frase5)

#Removendo um caracter especifico com o strip
frase6 = "*************Olá***********"
print(frase6.strip("*"))

#Concatenando de uma forma diferente
nome = "Luis Eduardo"
idade = 18
altura = 1.72
print(f"Meu nome é {nome}, tenho {idade} e minha altura é de {altura:.2f} metros")

#Deixando o texto todo em maiúsculo
print(frase.upper())

#Deixando o texto todo em minúsculo
print(frase.lower())

#Deixando apenas a primeira letra em maiúsculo
print(frase.capitalize())

#Contando a quantidade de letras dentro de uma frase
print(frase.count("o"))

#Subustituindo uma palavra especifica
print(frase.replace("mundo","amigo"))