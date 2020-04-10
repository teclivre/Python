print('\33[1;33m')
print('{:=^40}' .format('Desafio 53'))
print('{:=^40}' .format('Palíndromo'))
from time import sleep
f = str (input('Escreva uma frase: ')).strip().upper()
print('\n')
print('Um momento estamos análizando a frase...')
print('\33[m')
sleep(1)

f1 = f.split()
junto  = ''.join(f1)
print(f'{junto}')
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
     inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('Não é Palíndromo')
