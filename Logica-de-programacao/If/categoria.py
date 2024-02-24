nota = int(input("Digite a sua nota:\n"))
#trabalhando em uma só linha com três verificações de condição
categoria = "baixa" if nota <= 50 else "média" if nota <= 80 else "alta"
print(f"Sua categoria é {categoria}")