print('\33[1;31m Desafio')

print('''calculo da soma entre números impares que são multiplos de 3
do 1 até 500''')
from time import sleep
n = 0
for c in range(1,500,2):
    if c % 3 == 0:
        print(c)
        sleep(0.2)
    n += c

print('SOMANDO...')
sleep(2)
print('.')
sleep(2)
print('.')
sleep(1)
print(f'A soma dos valores é: {n}')



