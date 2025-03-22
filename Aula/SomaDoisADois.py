"""Faça a implementação agora considerando a soma de 2 a 2"""


def soma_dois(lista):
    if len(lista) == 0:
        print("Lista Vazia!!")
    elif len(lista) == 1:
        return lista[0]
    else:
        if len(lista) % 2 != 0:
            soma = 0
            for i in range(0, len(lista), 2):
                soma = soma + lista[i] + lista[i - 1]
            return soma - lista[len(lista) - 1]
        else:
            soma = 0
            for i in range(0, len(lista), 2):
                soma = soma + lista[i] + lista[i - 1]
            return soma


lista = [2000, 1500, 4000, 1200]
soma_lista = soma_dois(lista)
print(soma_lista)