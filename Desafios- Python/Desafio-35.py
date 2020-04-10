print('-=-'*20)
print(' Calcular o tamanho de três retas.')
print('-=-'*20)
print('\n\n')
straight1 = float (input('Digite o valor da primeira reta: '))
straight2 = float (input('Digite o valor da segunda reta: '))
straight3 = float (input('Digite o valor da terceira reta: '))
if straight1 < straight2 + straight3 and straight2 < straight1 + straight3 and straight3 < straight1 + straight2:
    print('Com os valores digitados, {:.2f}cm, {:.2f}cm, {:.2f}cm FORMAM UM TRIÂNGULO.'.format(straight1,straight2,straight3))
else:
    print('Com os valores digitados, {:.2f}cm, {:.2f}cm e {:.2f}cm NÃO FORMAM UM TRIÂNGULO.'.format(straight1,straight2,straight3))
