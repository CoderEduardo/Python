#Mostrando apenas as palavras que tem mais de 4 letras
palavras = ["Carro","Dia","Luis","Bia","Judas"]

for palavra in palavras:
    if len(palavra) >= 4:
        print(f"Palavras que tem mais de 4 letras: {palavra} \n")

