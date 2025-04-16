def Dano(poderB, nivel):
    if nivel == 0 or nivel == 1:
        return poderB
    else:
        return poderB * Dano(poderB, nivel-1)


poderB = int(input("Poder base: "))
nivel = int(input("Nível: "))

danoTotal = Dano(poderB, nivel)

print(f"Dano Total: {danoTotal}")