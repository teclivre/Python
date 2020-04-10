# Conversão de real para dolar.

print('\n \n Agora vamos ver quantos dolares você pode comprar com os Reais que está em sua carteira. \n \n ')

name = input('Primeiro me diga seu nome: ')
d = float (input('Dite o valor do dolar no dia de hoje: $'))
r= float (input('\n \n Agora me diga quanto você tem em sua carteira? R$'))


dollar = r*d

print('\n \n Olá, {} em sua carteira tem R${:.2f} e você pode comprar ${:.2f}.\n \n '.format(name,r,dollar))