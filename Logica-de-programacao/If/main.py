numero1 = 20
numero2 = 40
numero3 = 50

"""if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
elif numero1 == numero2:
    print(f"O número {numero1} é igual ao {numero2}")"""
    
#podemos usar o elif também para continuar a comparação

#Ao usar o and todas as comparações precisam ser verdadeiras

if numero1 < numero2 and numero1 < numero3:
    print(f"O {numero1} é o menor de todos")
else:
    print("O número 1 não é o menor de todos")