#starting conditions


name  = str(input('Digite seu nome!'))
Name = name.upper()
if Name == 'ROBERIO':
    print('Que nome bonito!')
else:
     print('Eita nome feio!')
print('Bom dia, {}!'.format(Name))
print('\n\n')
print('{}, Agora vamos ver sua média.'.format(Name))
print('Lembrando que você precisa de uma média minima de 6 para se aprovado.')
condition = str(input('Voce que saber sua nota? s/n? '))
Condition = condition.upper()
if Condition == 'S':
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    average = ((n1 + n2)/2)
    print('Sua média é: {:.1f}'.format(average))
    if average < 6:
        print('Reprovado:')
    else:
        print('Aprovado!') 
else: 
    print('Tenha um bom dia, {}!'.format(Name))
print('Fim!')    

