print('\33[m Desafio 45 \33[m')

from random import choice
from time import sleep

print('Jogo de Pedra, Papel e Tesoura:')
print('''
[PE] Para Pedra
[PA] Para Papel
[TE] Para Tesoura.''')

game = str(input('Escolha para jogar com o computador: '))
print('\33[1:35m JO \33[m')
sleep(1)
print('\33[1:35m KEN \33[m')
sleep(1)
print('\33[1:35m PO!!! \33[m')
sleep(1)
g = game.upper()
if g == 'PE':
    print('Você escolheu Pedra.')
elif g == 'PA':
    print('Você escolheu Papel.')
elif g == 'TE':
    print('Você escolheu Tesoura.')
else:
    print('Escolha uma das opões acima.')
pe = 'Pedra'
pa = 'Papel'
te = 'Tesoura'

list = [pe, pa, te]
choice(list)
l = choice(list)
print(f'O Computador escollheu {l}')
if l == pe and g == 'PA':
    print('\33[1;32mGANHOU!!\33[m')
if l == pa and g == "PE":
    print('\33[1;31mPERDEU!!!\33[m')
if l == pe and g == 'TE':
    print('\33[1;31mPERDEU!!!\33[m')
if l == te and g == 'PE':
    print('\33[1;32mGANHOU!!\33[m')
if l == pa and g == 'TE':
    print('\33[1;32mGANHOU!!\33[m')
if l == te and g == 'PA':
    print('\33[1;31mPERDEU!!!\33[m')
if l == te and g == "TE":
    print('\33[1;33mEMPATE!!!\33[m')
if l == pa and g == "PA":
    print('\33[1;33mEMPATE!!!\33[m')
if l == pe and g == "PE":
    print('\33[1;33mEMPATE!!!\33[m')
