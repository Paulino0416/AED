def Div(vet):
    if len(vet) <= 1:
        return vet
    meio = len(vet) // 2
    esquerda = vet[:meio]
    direita = vet[meio:]

    vet_esquerda = Div(esquerda)
    vet_direita = Div(direita)

    return Merge(vet_esquerda, vet_direita)


def Merge(vet_esquerda, vet_direita):
    i = 0
    j = 0
    vet_aux = []
    while i < len(vet_esquerda) and j < len(vet_direita):
        if vet_esquerda[i] < vet_direita[j]:
            vet_aux.append(vet_esquerda[i])
            i += 1
        else:
            vet_aux.append(vet_direita[j])
            j += 1

    vet_aux.extend(vet_esquerda[i:])
    vet_aux.extend(vet_direita[j:])

    return vet_aux


a = [2, 4, 1, 3, 5]
resultado = Div(a)

print(resultado)
