dobrar = lambda n: n * 2
print(dobrar(5))

status = lambda n: "Negativo" if n < 0 else ("Zero" if n == 0 else "Positivo")
print(status(-4))

lista = [("João",35),("Maria",25),("Pedro",40)]
pessoas_ordenadas = sorted(lista,key=lambda x:x[1])
print(pessoas_ordenadas)