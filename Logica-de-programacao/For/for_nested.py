#For nested é um for dentro do outro

"""for i in range(1,4):
    
    for j in range(1,4):
        print(f"i: {i}, j:{j}")"""
        
quadrado_impares = [x**2 for x in range(10) if x %2 != 0]
print(quadrado_impares)

texto = "Hello World"
#Recebendo dentro de uma variável somente as consoantes, eliminando as vogais
consoantes = [letra for letra in texto if letra.lower() not in "aeiou"]
print(consoantes)