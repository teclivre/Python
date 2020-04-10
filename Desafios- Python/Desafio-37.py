print('\33[1;31m Desafio 37 \33[m')

'''Escrevendo um programa que leia um número inteiro qualquer e peça para o usuário esclher qual será a base de conversão '''

number = int(input('Digite um número inteiro: '))

base = str(input('''Qual base deseja converter?
[B] para Binário
[O] Para Octal
[H] Para Hexadecimal \n'''))
base1 = base.capitalize()

b = bin(number)
o = oct(number)
h = hex(number)

if base1 == 'B':
    print(f'\33[1;32m O número {number} em binário é: {b[2:]} \33[m')
elif base1 == 'O':
    print(f'\33[1;32m O número {number} em Octal é: {o[2:]}  \33[m')
elif base1 =='H':
    print(f'\33[1;32m O número {number} em Hexadecimal é: {h[2:]} \33[m')
else:
    print('\33[1;31mEntrada invalida, tente novamente.\33[m')

# if b = 'Binário' or 'Octal' or 'Hexadecimal':
#   print('\33[1;31m Entrada invalida. \33[m')
