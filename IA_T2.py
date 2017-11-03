import random

def cria_caverna():
    lista_locais_usados = []

    Tabuleiro = []
    coluna = []
    for i in range(14):
        coluna.append(1)
    Tabuleiro.append(coluna)
    coluna = []
    coluna.append(1)
    for i in range (12):
        coluna.append(0)
    coluna.append(1)
    for i in range(12):
        Tabuleiro.append(coluna)
        
    coluna = []
    for i in range(14):
        coluna.append(1)
    Tabuleiro.append(coluna)
    
    #colocar os inimigos, buracos e barras de ouros que valem mais do que dinheiro
    
    
    lista_locais_usados.append([1,1])
    new_local=[]
    
    col_num = random.randint(1,13)
    lin_num = random.randint(1,13)
    new_local.append(col_num)
    new_local.append(lin_num)
    Tabuleiro[1][1] = 3
    if new_local not in lista_locais_usados[0]:
        lista_locais_usados.append(new_local)
        
        Tabuleiro[lin_num][col_num] = 3
    
    
    for i in Tabuleiro:
        
        print(i)

    
cria_caverna()
