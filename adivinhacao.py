import random

def jogar():

    print("Bem vindo no jogo de Adivinhação!")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 100

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Escolha o nível: '))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3


    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou:', chute)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if (maior):
                print('Você errou! O seu chute foi maior que o número secreto!')
            elif (menor):
                print('Você errou! O seu chute foi menor que o número secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (total_de_tentativas == rodada):
                print(f'O número secreto era {numero_secreto} e você fez {pontos} pontos!')

    print('Fim de jogo!')

if (__name__ == '__main__'):
    jogar()