def Soma_Lista(lista):
    cont = 0
    soma = 0
    while cont != len(lista):
        if len(lista) == 0:
            print("Lista Vazia!!")
            break
        elif len(lista) == 1:
            cont+= 1
            return lista[0]
        else:
            soma += lista[cont]
            cont += 1
    return soma


lista = [2000, 1500, 4000, 1200]
Soma_Lista = Soma_Lista(lista)
print(Soma_Lista)
