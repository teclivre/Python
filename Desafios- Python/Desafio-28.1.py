from random import randint
from time import sleep
think = randint(1, 10) #faz o computador pansar.
print('-=-'*20)
print('Vou pensar em um número, adivinhe qual é: ')
print('-=-'*20)
game = int (input('Digite um número de 1 a 10: '))
print('Processando...')
sleep(3)
if game == think:
    print('Você acertou, pansei no número {}.'.format(think))
else:
    print('Você errou Pensei no número {}.'.format(think))