#São funções que chamam a si mesmo

def decrementar(n):
    
    if n > 0:
        print(n)
        decrementar(n - 1)
        
decrementar(10)

#Uma forma de deixar a sua função comentada para outro programador acessar e retornar o documento é o .__doc__, onde o comentário vai retornar
#o que estiver comentado dentro da função

def fatorial(n):
    
    """
    Função que calcula o n fatorial, ela recebe como parâmetro um número e retorna o seu resultado
    """
    
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
print(fatorial(5))
#No cmd vai aparecer o comentário dentro da função
print(fatorial.__doc__)

#Type Hits
#Deixando claro o tipo de dados que uma função vai receber e retornar
def multiplicar(n1:int,n2:int) -> int:
    return n1 * n2 
#Eu deixo claro que a função recebe números inteiros e retorna números inteiros
print(multiplicar(5,20))
        
        
        
        
        
        
        