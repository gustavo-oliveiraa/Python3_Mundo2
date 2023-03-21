from random import randint
computador = randint(0, 10)  # faz o computador "PENSAR" em um número
acertou = False
palpites = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
while not acertou:
    jogador = int(input('Qual é seu palpite? '))  # jogador tenta advinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
