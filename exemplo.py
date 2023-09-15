matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz)

print(matriz[1]) # volta a linha toda

print(matriz[1][2]) # volta a linha e a coluna

matriz[0][1] = 100 # altera o valor na linha e coluna colocada
print(matriz)

# para mostrar como uma matriz mesmo
for linha in matriz:
    for item in linha:
        print(item)

for linha in matriz:
    for item in linha:
        print(item, end='\t') # espaço igual com tab para facilitar formatação
    print()

# Com inputs do usuário

linhas = int(input("Informe a quantidade de linhas: "))

colunas = int(input("Informe a quantidade de colunas: "))

matrizInput = []

for linha in range(linhas):
    lista = []
    for coluna in range(colunas):
        n = int(input("Número: "))
        lista.append(n)
    matrizInput.append(lista)

print(matrizInput)

def exibeMatriz(matriz): # função para formatar matriz
    for linha in matriz:
        for item in linha:
            print(item, end='\t')
        print()

# Matriz sempre usa for

# percorrer itens da matriz 
cont = 0
for linha in matriz:
    for item in linha:
        if item % 2 == 0:
            cont += 1
print(cont)

# percorrer indices da matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 100 # muda os valores a partir do indice -> para 100, nesse caso
exibeMatriz(matriz)