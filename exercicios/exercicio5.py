'''
    Exercício 5:
    Preencha uma matriz 10x10 com números aleatórios e exiba a matriz. A seguir, exiba o somatório dos 
    elementos da diagonal secundária da matriz
'''

import random

matriz = []

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

for linha in range(10):
    lista = []
    for coluna in range(10):
        lista.append(random.randint(1, 500))
    matriz.append(lista)

exibeMatriz(matriz)

cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i + j == (len(matriz) - 1):
            cont += matriz[i][j]

print(cont)