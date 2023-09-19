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

# Já pede 15 digitos para o usuário
for linha in range(3):
    lista = []
    for coluna in range(5):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    matriz.append(lista)

exibeMatriz(matriz)

# Percorrer a matriz para então trocar os valores
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 100:
            matriz[i][j] = 0

print(f"A matriz modificada é")
exibeMatriz(matriz)