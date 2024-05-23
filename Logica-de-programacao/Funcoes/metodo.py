"""def saudacao():
    return "Olá, Mundo"

cumprimentar = saudacao 

#Uma função consegue herdar a outra, executando as duas da mesma forma dentro de uma variável
#Atribuindo função há uma variável
print(saudacao())
print(cumprimentar())"""

#Passando funções por argumentos
def saudacao_nome(nome):
    return f"Ola, {nome}"

def cumprimentar(funcao,nome):
    return funcao(nome) 

print(cumprimentar(saudacao_nome,"Luis Eduardo"))

#Retornando funções de outras funções

def nivel_saudacao(nivel):
    
    def saudacao_basica():
        return ("Oi")
    
    def saudacao_avançada():
        return ("Olá, como você está?")
    
    if nivel == "basico":
        return saudacao_basica
    elif nivel =="avancada":
        return saudacao_avançada

conversar = nivel_saudacao("avancada")
print(conversar())
    