'''
    Exercício 3:
    Solicite ao usuário 15 valores e armazene em uma matriz 3x5 e exiba a matriz. A seguir, troque todos 
    os elementos da matriz que sejam maiores do que 100 pelo valor zero e exiba a matriz novamente.
'''

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

