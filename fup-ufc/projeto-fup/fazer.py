import os
import time
import random

def limparTela():
    os.system("cls")

def mostrarTabuleiro(tabuleiro):
    print("\tJOGO DA VELHA")
    print("\t+---+---+---+")
    for i in range(3):
        print("\t|", end="")
        for j in range(3):
            print(f" {tabuleiro[i][j]} |", end="")
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

pontos = {jogador1: 0, jogador2: 0}

continuar = True 

while continuar:
    sorteio = random.sample("XO",1)
    tabuleiro = criarTabuleiro()
    jogadorAtual = sorteio[0]

    while True: 
        limparTela()
        mostrarPlacar(jogador1, jogador2, pontos)
        mostrarTabuleiro(tabuleiro)
        
        if jogadorAtual == "X":
            nomeAtual = jogador1
        else:
            nomeAtual = jogador2

        try:
            posicao = int(input(f"\n{nomeAtual} [{jogadorAtual}], escolha sua posição (1/9): "))

            if not jogar(tabuleiro, jogadorAtual, posicao):
                print("Jogada Inválida! Tente novamente.")
                time.sleep(1)
                continue
        except ValueError:
            print("Digite apenas números!")
            time.sleep(1)
            continue

        if verificarVitoria(tabuleiro):
            limparTela()
            mostrarTabuleiro(tabuleiro)
            print(f"\n {nomeAtual} venceu!")
            pontos[nomeAtual] += 1
            break

        if verificarEmpate(tabuleiro):
            limparTela()
            mostrarTabuleiro(tabuleiro)
            print("\nEmpate! Ninguém venceu.")

        jogadorAtual = trocarJogador(jogadorAtual)
    resposta = input("Deseja jogar novamente?(s/n)").lower()
    if resposta != "s":
        continuar = False

    limparTela()
    mostrarPlacar(jogador1, jogador2, pontos)
    print("Obrigado por jogar!!!")




