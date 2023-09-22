'''
    Exercício 3:
    Solicite ao usuário 15 valores e armazene em uma matriz 3x5 e exiba a matriz. A seguir, troque todos 
    os elementos da matriz que sejam maiores do que 100 pelo valor zero e exiba a matriz novamente.
'''
import moduloMatriz

matriz = moduloMatriz.preencheMatriz(3, 5)
moduloMatriz.exibeMatriz(matriz)

# Percorrer a matriz para então trocar os valores
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 100:
            matriz[i][j] = 0

print(f"A matriz modificada é")
moduloMatriz.exibeMatriz(matriz)