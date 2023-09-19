'''
    Exercício 6:
    Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, informe o menor 
    elemento da matriz.
'''

import random

matriz = []

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

for linha in range(5):
    lista = []
    for coluna in range(5):
        lista.append(random.randint(1, 100))
    matriz.append(lista)

exibeMatriz(matriz)

menorValor = None
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if menorValor is None or matriz[i][j] < menorValor:
            menorValor = matriz[i][j]

print(f"O menor valor da matriz é de {menorValor}")