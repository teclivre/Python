print('\33[1;31;40m Desafio 46 \33[m')
print('\n')
print('''\33[1;31mprograma mostra na tela contagem regrassiva para estouro de fogos de artificio,
indo de 10 até 0, com pausa de 1 segundo entre eles\33[m''')
start = int(input('Didite o número que deseja iniciar: '))
from time import sleep
from emoji import demojize
for start in range(start,0,-1):
    sleep(1)
    print(start)
sleep(2)
print('======BOMMM!!!=========')
print(emoji.demigize(':bomb:'))

