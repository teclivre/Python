print('\33[1;31m')
print('{:=^40}' .format(' DESAFIO 50 '))
print('\33[m \n')
from time import sleep
n1 = 0
for c in range(0,6):
    c = int(input('Digite um valor: '))
    if c % 2 == 0:

        n1 += c
print('Somando os números pares...')
sleep(2)
print(f'A Soma dos números pares é: {n1}')
print('FIM!')



