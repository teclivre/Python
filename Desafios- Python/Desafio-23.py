number = int (input('Informe um número: '))
print(' \n\n Análisando o número: {}'.format(number))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))