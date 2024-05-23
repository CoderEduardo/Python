animais = []
animais.append("Gato")
animais.append("Cachorro")
animais.append("Pássaro")
print(animais)
animais.insert(1,"Peixe")
print(animais)
animais.remove("Gato")
print(animais)
animal_removido = animais.pop()
print(animais)
novos_animais = ["Tartarugas","Hamster"]
print(novos_animais)
todos_animais = animais + novos_animais
print(todos_animais)
animais_duplicados = todos_animais * 2
print(animais_duplicados)
if "Cachorro" in todos_animais:
    print("Cachorro está na lista")
else:
    print("Cachorro não está na lista")