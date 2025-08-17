valor = float(input("Digite o valor da compra:\n"))

if valor <= 500:
    print("Você não tem desconto")
    desconto = valor
elif valor <= 1000:
    print("Você tem 10 % de desconto")
    desconto = valor-(valor * 0.10)
else:
    print("Você tem 20 % de desconto")
    desconto = valor-(valor * 0.20) 
    
print(f"O valor total a se pagar é de {desconto:.2f}")

print("Teste")