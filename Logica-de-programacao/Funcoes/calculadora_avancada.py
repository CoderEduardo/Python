from functools import reduce
import operator

def fabrica_de_funcoes(operacao):
    
    def somar(*args):
        return sum(args)
    
    def subtrair(*args):
        return reduce(operator.sub,args)
    
    def multiplicar(*args):
        return reduce(operator.mul,args)
    
    def dividir(*args):
        return reduce(lambda x, y: x / y, args)
    
    if operacao == "adicionar":
        return somar
    elif operacao == "subtrair":
        return subtrair
    elif operacao == "multiplicar":
        return multiplicar
    elif operacao == "dividir":
        return dividir
    else:
        print("Operação inválida!!!")
    
adicionar = fabrica_de_funcoes("adicionar")
subtrair = fabrica_de_funcoes("subtrair")
dividir = fabrica_de_funcoes("dividir")
multiplicar = fabrica_de_funcoes("multiplicar")

print(adicionar(10,20,100,70))
print(subtrair(50,20,15))
print(dividir(20,2,5))
print(multiplicar(5,6,2,5))