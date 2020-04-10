print('\33[1;30;45m Desafio 38 \33[m')
print('\n\n')
'''Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeiro número é maior
- O Segundo número é maior
- Os números São iguais'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número:'))

if n1 > n2:
    print(f'O número{n1} é maior que {n2}.')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}.')
else:
    print('Os Valores São iguais.')

print('\n \33[1:37m Fim!!! \33[m')
