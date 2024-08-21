#listas aninhadas são listas dentro de listas

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[1][2])

for linha in matriz:    #primeiro percorremos as linhas de uma matriz

    for numero in linha:    #depois os números dentro de uma linha

        print(numero)       #e no final exibimos todos eles

total = 0

for linha in matriz:    

    for numero in linha:    
        total += numero

print(total)