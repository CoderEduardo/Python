nome = "Maria"
sobrenome = "Silva"
idade = 30
nome_completo = f"{nome} {sobrenome}"
print(nome_completo)

#Usando o format para concatenar as variáveis
mensagem = "Olá meu nome é {}, e tenho {} anos".format(nome_completo,idade)
print(mensagem)

frase = "Python é uma linguagem de programação poderosa e versátil"
#Vendo a quantidade de caracteres de uma frase
tamanho_frase = len(frase)
print(tamanho_frase)

#Recortando a primeira palabra da frase
palavra = frase.split()[0]
print(f"Primeira palavra da frase: {palavra}")

#deixando a frase maiúscula
frase_maiuscula = frase.upper()
print(frase_maiuscula)

#substituindo uma palavra
frase_substituida = frase.replace("poderosa","incrivel")
print(frase_substituida)