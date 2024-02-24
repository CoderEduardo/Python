print("Responda com sim ou não\n")
convite = input("Você tem um convite vip?\n").lower()
lista = input("Você está na lista de convidados?\n").lower()
membro = input("Você é membro do clube?\n").lower()

if convite == "sim" or lista == "sim" or membro == "sim":
    print("Você pode entrar")
else:
    print("Você não pode entrar")