"""for i in range (1,11):
    print(i)
    
#O terceiro argumento é o passo que sera decrementado em cada loop
for i in range (10,0,-1):
    print(i)
    
for i in range (0,11,+2):
    print(i)"""
    
#Somando os números impares
soma = 0

for i in range(1,11,+2):
    print(f"Número impar atual: {i}")
    soma += i

print(f"Soma dos números impares: {soma}")