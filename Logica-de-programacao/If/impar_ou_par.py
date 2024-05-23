numero = int(input("Digite um número\n"))

"""if numero%2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar") """
    

#usando operador ternário
resultado = "par" if numero%2 == 0 else "impar"
print(f"O número {numero} é {resultado}")