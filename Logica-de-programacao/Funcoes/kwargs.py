#Com o kwargs podemos nomear argumentos e passar eles para função ser ter definido eles preveamente

def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
        
exibir_informacoes(nome="Lucas",estado="São Paulo",idade = 30)