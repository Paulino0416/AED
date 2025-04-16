def TempoDiv(lista):
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        es = TempoDiv(lista[:meio])
        di = TempoDiv(lista[meio:])

        return Merge(es, di)


def Merge(es, di):
    i = 0
    j = 0
    lista_comp = []
    while i < len(es) and j < len(di):
        if es[i] < di[j]:
            lista_comp.append(es[i])
            i += 1
        else:
            lista_comp.append(di[j])
            j += 1

    lista_comp.extend(es[i:])
    lista_comp.extend(di[j:])

    return lista_comp


quantPil = int(input("Quantidade de pilotos: "))
lista = []

for i in range(1, quantPil + 1):
    lista.append(int(input(f"Tempo do piloto {i}: ")))

resultado = TempoDiv(lista)
print(f"Tempos ordenados: {resultado}")