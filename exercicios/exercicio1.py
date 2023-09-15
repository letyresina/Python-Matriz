'''
    Exercício 1:
    Preencha uma matriz 3x5 com números inteiros informados pelo usuário e exiba a matriz.
'''

matriz = []

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

for linha in range(3):
    lista = []
    for coluna in range(5):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    matriz.append(lista)

exibeMatriz(matriz)