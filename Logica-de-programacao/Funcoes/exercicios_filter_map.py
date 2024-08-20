numeros = [2,5,8,10,12,15,18,20,23,25,28]
#filtrado números impares
numerosImpares = list(filter(lambda x: x % 2 != 0,numeros))
#elevando ao quadrado os números impares
quadradoNumerosImpares = list(map(lambda x: x**2, numerosImpares))
print(numerosImpares)
print(quadradoNumerosImpares)
