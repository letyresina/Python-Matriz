def preencheMatriz(lin:int, col:int) -> list:
    '''
        Preencher uma matriz
    '''
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            num = int(input("Informe o numero: "))
            linha.append(num)
        matriz.append(linha)
    return matriz

def exibeMatriz(matriz: list) -> None: 
    '''
        Exbir matriz formatada
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()
            
        