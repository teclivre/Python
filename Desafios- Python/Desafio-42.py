print('\33[1;30;44m Desafio 42 \33[m')
print('\n')

straigtht1 = float(input('Entre com o primeiro dado do triângulo: '))
straigtht2 = float(input('Entre com o segundo dado do triângulo: '))
straigtht3 = float(input('Entre com o terceiro dado do triângulo '))

if straigtht1 < straigtht2 + straigtht3 and straigtht2 < straigtht1 + straigtht3 and straigtht3 < straigtht1 + straigtht2:
    print('Essas retas fotmam um triângulo.', end='')
    if straigtht1 == straigtht2 == straigtht3:
        print('EQUILATERO.')
    if straigtht1 != straigtht2 != straigtht3 != straigtht1:
        print('ESCALENO.')
    else:
        print('ISÓCELES')
else:
    print('Essas retas não formam um triângulo.')


