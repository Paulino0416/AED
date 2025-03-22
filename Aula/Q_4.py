def MuroInfinito(lista, inicio, elemento):
    s = 0
    if elemento == lista[inicio]:
        return inicio
    else:
        while lista[inicio + s] != elemento and lista[inicio - s] != elemento:
            s += 1
            if lista[inicio + s] == elemento:
                return lista[inicio + s]
            elif lista[inicio - s] == elemento:
                return lista[inicio - s]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = int(input('Elemento a ser encontrado: '))
inicio = int(input('Inicio da lista: '))

print(MuroInfinito(lista, inicio, elemento))
