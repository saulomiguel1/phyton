import os
import time


# -------------------------------
# FUNÇÕES AUXILIARES
# -------------------------------

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_tabuleiro(tabuleiro):
    """Mostra o tabuleiro do jogo"""
    print("     JOGO DA VELHA")
    print("   +---+---+---+")
    for i in range(3):
        print("   |", end="")
        for j in range(3):
            print(f" {tabuleiro[i][j]} |", end="")
        print("\n   +---+---+---+")


def trocar_jogador(jogador):
    """Alterna entre X e O"""
    return "O" if jogador == "X" else "X"


def jogar(tabuleiro, jogador, posicao):
    """Executa a jogada"""
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == str(posicao):
                tabuleiro[i][j] = jogador
                return True
    return False


def verificar_vitoria(tabuleiro):
    """Verifica se alguém venceu"""
    # Linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            return True

    # Colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j]:
            return True

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return True

    return False


def verificar_empate(tabuleiro):
    """Verifica empate"""
    for linha in tabuleiro:
        for valor in linha:
            if valor not in ["X", "O"]:
                return False
    return True


def criar_tabuleiro():
    """Cria um novo tabuleiro numerado"""
    tabuleiro = []
    contador = 1
    for _ in range(3):
        linha = []
        for _ in range(3):
            linha.append(str(contador))
            contador += 1
        tabuleiro.append(linha)
    return tabuleiro


def mostrar_placar(jogador1, jogador2, pontos):
    """Exibe o placar"""
    print("📊 PLACAR")
    print(f"{jogador1}: {pontos[jogador1]} vitória(s)")
    print(f"{jogador2}: {pontos[jogador2]} vitória(s)")
    print("-" * 25)


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

limpar_tela()
print("🎮 Bem-vindo ao Jogo da Velha!\n")

jogador1 = input("Nome do jogador X: ")
jogador2 = input("Nome do jogador O: ")

pontos = {jogador1: 0, jogador2: 0}

continuar = True

while continuar:
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    while True:
        limpar_tela()
        mostrar_placar(jogador1, jogador2, pontos)
        mostrar_tabuleiro(tabuleiro)

        nome_atual = jogador1 if jogador_atual == "X" else jogador2

        try:
            posicao = int(input(f"\n{nome_atual} [{jogador_atual}], escolha uma posição (1-9): "))

            if not jogar(tabuleiro, jogador_atual, posicao):
                print("❌ Jogada inválida!")
                time.sleep(1)
                continue

        except ValueError:
            print("❌ Digite apenas números!")
            time.sleep(1)
            continue

        if verificar_vitoria(tabuleiro):
            limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print(f"\n🏆 {nome_atual} venceu!")
            pontos[nome_atual] += 1
            break

        if verificar_empate(tabuleiro):
            limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print("\n🤝 Empate!")
            break

        jogador_atual = trocar_jogador(jogador_atual)

    resposta = input("\nDeseja jogar novamente? (s/n): ").lower()
    if resposta != "s":
        continuar = False

limpar_tela()
mostrar_placar(jogador1, jogador2, pontos)
print("🎯 Obrigado por jogar!")