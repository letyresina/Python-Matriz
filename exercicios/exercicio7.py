'''
    Exercício 7:
    Preencha uma matriz 5x4 com números informados pelo usuário e exiba a matriz. Em seguida, solicite 
    um número e faça uma busca na matriz por esse número, informando a posição onde ele se encontra 
    (índice da linha e índice da coluna). Se o número aparecer mais de uma vez na matriz, exiba todas as 
    posições onde ele foi encontrado.
'''

matriz = []

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

for linha in range(5):
    lista = []
    for coluna in range(4):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    matriz.append(lista)

exibeMatriz(matriz)

# Para encontrar valores dentro da matriz

numero = int(input("Informe o número para buscar na matriz: "))

posicoesEncontradas = [] # armazena em uma lista caso seja mais de uma

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == numero:
            posicoesEncontradas.append((i, j))

if posicoesEncontradas:
    print(f"O número {numero} foi encontrado nas posições:")
    for posicao in posicoesEncontradas:
        print(f"Linha: {posicao[0]} Coluna: {posicao[1]}")
else:
    print(f"O {numero} não foi encontrado na matriz!")