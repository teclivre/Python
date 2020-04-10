print('\33[1;33m')
print('{:=^40}' .format(' Desafio 52 '))
print('{:=^40}' .format(' Número Primo '))
print('\33[m')


n = int(input("Didite um número: "))
if n == 0:
    print(f'O número {n} é Primo')
elif n%2 == 1:
    print(f'O número {n}, é Primo.')
else:
    print(f'O número {n}, não é primo.')


