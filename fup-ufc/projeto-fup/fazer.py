def mostrarJogo(tabuleiro):
    print("   JOGO DA VELHA")
    print("   +---+---+---+")
    for i in range(3):
        print("   |", end="")
        for j in range(3):
            print("   |", end="")
        print("\n   +---+---+---+")

def criarJogo():
    tabuleiro = []
    contador = 1   


print ("Bem vindo ao jogo da velha!")
jogador1 = input("\nNome de quem será o jogador X: ")
jogador2 = input("Nome de quem será o jogador O: ")


