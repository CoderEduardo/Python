frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
print("Lista de frutas:", frutas)
frutas.append('kiwi')
print("Lista de frutas após adicionar kiwi:", frutas)
frutas.remove('banana')
print("Lista de frutas após remover banana:", frutas)

for fruta in frutas:
    print(f"Eu gosto de {fruta}!")

amigos = ['Alice', 'Bob', 'Carlos', 'Diana', 'Eduardo']
for amigo in amigos:
    print(f"Olá, {amigo}! Como você está?") 