from time import sleep
print('\33[1:31m')
print('{:=^40}' .format('Desafio 51'))
print('\33[m \n')
print('\33[1:33m')
print('''Programa que realiza a leitura do primeiro termo
e a razão de um PA. NO final, mostrará os 10 primeiros 
termos dessa prograssão.''')
print('\33[m \n')
p = int(input('Digite i primeiro termo: '))
r = int(input('Digite a razão:'))
t = int(input('Digite quantos termos: '))
for c in range(1,t):
    print(p)
    sleep(0.5)
    p += r
print('FIM!!!')
