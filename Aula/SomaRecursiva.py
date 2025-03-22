"""Implemente o mesmo problema anterior usando uma solução recursiva."""



def soma_recursiva(lista):
    if len(lista) == 0:
        print("Lista Vazia!!")
    elif len(lista) == 1:
        return lista[0]
    else:
        meio = len(lista) // 2
        lista_esquerda = soma_recursiva(lista[:meio])
        lista_direita = soma_recursiva(lista[meio:])
        return lista_esquerda + lista_direita


Lista = [2000, 1500, 4000, 1200]
Soma_Lista = soma_recursiva(Lista)
print(Soma_Lista)