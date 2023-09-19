'''
    Exercício 8:
    Preencha uma matriz 4x4 com números informados pelo usuário e exiba a matriz. Na sequência, gere 
    a transposta da matriz e exiba-a (matriz transposta é a matriz que se obtém da troca de linhas por 
    colunas da matriz)
'''

matriz = []

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

for linha in range(4):
    lista = []
    for coluna in range(4):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    matriz.append(lista)

exibeMatriz(matriz)

matrizTransposta = []

for i in range(len(matriz[0])):
    linhaTransposta = []
    for j in range(len(matriz)):
        linhaTransposta.append(matriz[j][i])
    matrizTransposta.append(linhaTransposta)

print("Matriz Transposta")
exibeMatriz(matrizTransposta)