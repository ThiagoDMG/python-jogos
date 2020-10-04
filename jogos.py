import forca
import adivinhacao
#titulo2
def escolher_jogo():

    print("Escolha o seu Jogo!")

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual jogo? '))
#lista3
    if (jogo == 1):
        print('Jogando Forca!')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando Adivinhação!')
        adivinhacao.jogar()

if (__name__ == '__main__'):
    escolher_jogo()

#edit    