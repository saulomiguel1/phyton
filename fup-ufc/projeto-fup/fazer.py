import os
import time

def limparTela():
    os.system("cls")

def mostrarTabuleiro(tabuleiro):
    print("\tJOGO DA VELHA")
    print("\t+---+---+---+")
    for i in range(3):
        print("\t|", end="")
        for j in range(3):
            print(f"{tabuleiro[i][j]} |", end="")
        print("\n\t+---+---+---+")

def trocarJogador(jogador):
    if jogador == "X":
        return "O"
    else: 
        return "X"
    
def jogar(tabuleiro, jogador, posicao):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == str(posicao):
                tabuleiro[i][j] = jogador
                return True
    return False

def verificarVitoria(tabuleiro):
    #Pela horizontal
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            return True
    #Pela vertical
    for j in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]:
            return True
    #Pela diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return True    
    #Deu velha
    return False

def verificarEmpate(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor not in ["X", "O"]:
                return False
    return True

def criarTabuleiro():
    tabuleiro = []
    contador = 1
    for lin in range(3):
        linha = []
        for col in range(3):
            linha.append(str(contador))
            contador += 1
        tabuleiro.append(linha)
    return tabuleiro

def mostrarPlacar(jogador1, jogador2, pontos):
    print("PLACAR")
    print(f"{jogador1}: {pontos[jogador1]} vitória(s)")
    print(f"{jogador2}: {pontos[jogador2]} vitória(s)")
    print("-"*25)

#--------------------------------------------------------------------------------------------------------------------------------------------------

limparTela()
print("Bem vindo ao JOGO DA VELHA!")

jogador1 = input("Nome do jogador que usará o X: ")
jogador2 = input("Nome do jogador que usará o O: ")




