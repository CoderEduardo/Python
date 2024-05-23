"""def soma (a,b):
    return a + b 

print(soma(20,30))"""

#Com args conseguimos usar vários métodos do python para manipular os argumentos

def soma (*args):
    resultado = sum(args)   #sum() é um método que soma todos elementos passados por parâmetro
    print(resultado)
    
soma(2,5,6,75,10)