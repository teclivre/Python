print('\n\n')
print('-=-'*40)
print('''Sua velocidade máxima é 80 km/h, se você ultapassar essa velocidade será multado em R$7,00 por km ultrapassado.''')
print(('-=-'*40))
print('\n')
Speed = float(input('Informe a velocidade do veículo: \n\n'))

c = Speed - 80
m = c*7
if Speed > 80:
    print('Você está a {}km/h e está acima do permitido, portanto, pagará R${:.2f} de multa por ter infringido a lei de transito.'.format(Speed,m))
else:
    print('Parabéns você está respeitando os limítes de velocidade.')
    print('---'*30)