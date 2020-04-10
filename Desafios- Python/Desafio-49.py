print('\33[1;31 Desafio 49 \33[m')
print('\n\n Tebuada')
from time import sleep
t = int(input('Digite o número para fazer a tabuada: '))

for c in range(1,11):
     print(f'{ t} x {c } = { t*c}')
     sleep(0.4)
