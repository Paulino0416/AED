"""Você recebeu a tarefa de implementar uma função que calcule a soma de todos os
salários contidos em um array de tamanho n. Cada elemento do array representa o
salário de um funcionário. Sua função deve receber esse array de salários e retornar
(ou imprimir) o valor total da soma de todos eles.
Requisitos:
• A função deve aceitar um array de inteiros que representam os salários.
• A função deve retornar (ou imprimir) a soma de todos os valores presentes
no array.
• Caso o array esteja vazio, a função deve retornar (ou imprimir) zero.
Exemplo de entrada/saída:

• Entrada: [2000, 1500, 4000, 1200]
• Saída: 8700"""


def Soma_Lista(lista):
    cont = 0
    soma = 0
    while cont != len(lista):
        if len(lista) == 0:
            print("zero")
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
