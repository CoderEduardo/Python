def estatisticas(*args):
    
    #Retorna o maior valor do conjunto
    print("Maior Número: ", max(args))
    #Retorna o menor valor do conjunto
    print("Menor número: ", min(args))
    #Usa o sum para calcular o valor total e depois dividir pelo número de elementos, assim, fazendo a média
    media = sum(args) / len(args)
    print(f"Média: {media:.2f}")    


#Aplicando float em todos os itens de uma lista
numeros = list(map(float,input("Digite a sequência de números por espaços\n").split()))

estatisticas(*numeros)

"""textos = [3,5,7,8,9,35]
print(max(textos))"""

