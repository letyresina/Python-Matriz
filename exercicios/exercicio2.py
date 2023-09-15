'''
    Exercício 2:
    Preencha uma matriz 6x6 com o elemento 1 em todas as posições em que o índice de linha tem valor 
    igual ao índice da coluna. Preencha os demais elementos com zero e exiba a matriz.
'''

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

matriz = []

'''matriz = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
]'''

for linha in range(6):
    lista = []
    for coluna in range(6):
        if linha == coluna:
            num = 1
            lista.append(num)
        else: 
            num = 0
            lista.append(num)
        
    matriz.append(lista)

exibeMatriz(matriz)