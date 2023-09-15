'''
    Exercício 3:
    Solicite ao usuário 15 valores e armazene em uma matriz 3x5 e exiba a matriz. A seguir, troque todos 
    os elementos da matriz que sejam maiores do que 100 pelo valor zero e exiba a matriz novamente.
'''

matriz = []

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

for i in range(15):
    for linha in range(3):
        num = int(input("Informe um número inteiro: "))
        lista = []
        for coluna in range(5):
            lista.append(num)
        matriz.append(lista)

exibeMatriz(matriz)