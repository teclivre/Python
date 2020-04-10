from random import choice
print('==----=='*10)
print('Agora vamos jogar!')
print('==----=='*10)
print('Adivinhe o número que o computador pensou.')

n1 = 1
n2 = 2
n3 = 3
n4 = 4 
n5 = 5
n6 = 6
n7 = 7
n8 = 8
n9 = 9
n10 = 10
number = int(input('Escolha um número de 1 a 10: '))
print('Você escolheu o número: {}'.format(number))
print('\n')
n11 = choice([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10])
print('O computador pensou em: {}'.format(n11))

if n11 == number:
    print('Você acertou, o computador pensou no número {} e você também.'.format(n11))
else:
    print('Você errou o computador pensou no número {} e você no número {}'.format(n11, number))
