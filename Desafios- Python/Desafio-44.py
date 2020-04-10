print('\33[1;44mDesafio 44 \33[m')

print('{:=^40}' .format("TECLIVRE"))
print('\n\n')

'''Programa que realiza cálculo de valor a ser pago considerando a forma de pagamento.

- à vista dinheiro, cheque ou dédito 10% de desconto.
- Cartão de crédito a vista 5% de  deesconto.
- Cartão de crédito em 2x preço sem desconto.
- cartão de crédito em 3x ou mais 20% de acrescimo.
'''

n = str(input('Digite seu name: '))
name = n.upper()
print(f'Olá {name}, tudo bem?')
print('\n')

value = float(input('Digite o valor de sua compra: R$'))
print(f'Muito bem, {name}. O valor de sua compra é R${value}')
print('''
[1] para compra à vista 
[2] para crédito a vista
[3] para parcelar em duas vezes no cartão
[4] para parcelar em três  ou mais vezes no cartão''')
pay = int(input('\33[1;33mOpção de pagamento? \33[m'))

v1  = value - (value * 0.10)
c1  = value - (value * 0.05)
p3 = value + (value * 0.20)

if pay == 1:
    print(f' O calor de sua compra é R${value :0.2f}.')
    print('Você pagará a vista no dinheiro, Débito ou cheque.')
    print(f'O Valor com desconto  de 10% é R${v1 :0.2f}')
elif pay == 2:
    print(f'O valor de sua compra é R${value :0.2f}')
    print(f'Você pagará no crédito à vista.')
    print(f'O valor total com 5% de desconto é R${c1 :0.2f}')
elif pay == 3:
    print(f'O Valor de sua compra é R${value :0.2f}')
    print(f'Você pagará em 2x no cartão de cédito sem juros.')
    print(f'O valor total de x2 de R${value/2 :0.2f}')
if pay == 4:
    print(f'O valor de sua compra é R${value :0.2f}')
    parc = int(input('Em quantas parcelas deseja pagar? '))
    p = p3 / parc
    print('Você terá uma taxa de juros de 20%')
    print(f'Total a pagar de {parc}x de R${p :0.2f}, Total de {p3 :0.2f}.')
else:
    print('\33[1;31m Opção se pagamento invalida.\33[m')
