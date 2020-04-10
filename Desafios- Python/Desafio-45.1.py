from random import randint
from time import sleep
game = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
print('''Suas opçoes:
[0] Pedra
[1] Papel
[2] tesoura''')
print('='*24)
player = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('O computador escolheu: {}'.format(game[computer]))
print('Você escolheu: {}'.format(game[player]))
print('='*24)
if computer == 0: # Computador jogou pedra
    if player == 0:
        print("Empate")
    elif player == 1:
        print('Ganhou')
    elif player ==2:
        print('Perdeu')
    else:
        print('Jogada invalida')
if computer == 1: #Computer jogou Papel
    if player == 0:
        print('Perdeu')
    elif player == 1:
        print('Empate')
    elif player == 2:
        print('Ganhou')
    else:
        print('Jogada imvalida')
if computer == 2: #Computer joga tesoura
    if player == 0:
        print('Ganhou')
    elif player == 1:
        print('Perdeu')
    elif player == 2:
        print('Empate')
    else:
        print('Jogada invalida')

