#Iteração em listas

frutas = ['Maçã','Banana','Cereja','Damasco','Figo']

#Forma tradicional
for fruta in frutas:
    print(fruta)

#Dessa forma conseguimos acessar o índice do elemento
for indice, fruta in enumerate(frutas):
    print(f"A fruta no índice {indice} é {fruta}")

#Exercícios
notas = [85,90,78,92,88]
nomes = ['Alice','Bruno','Clara','Daniel','Eduarda']

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f"O nome no índice {indice} é {nome}")

for indice, nota in enumerate(notas):
    print(f"O aluno {nomes[indice]} tirou a nota {nota}")
