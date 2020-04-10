print('\n Agora iremos calcular o valor de sua passagem, conforme a distância de sua viagem. \n\n')

distance = int (input('Diga a distância da sua viagem em KM: '))

d1 = distance * 0.50
d2 = distance * 0.45

if distance <= 200:
    print('Sua Viagem é de {}km e você pagará R${:.2f}'.format(distance,d1))
else:
    print('Sua Viagem é de {}km e Você pagará R${:.2f}'.format(distance,d2))
print('\n Fim.')