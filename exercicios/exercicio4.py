'''
    Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, calcule o somatório dos 
    elementos da diagonal principal da matriz.
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
        lista.append(random.randint(1, 500))
    matriz.append(lista)

exibeMatriz(matriz)

cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            cont += matriz[i][j]

print(f"O somatório das diagonais é de {cont}")